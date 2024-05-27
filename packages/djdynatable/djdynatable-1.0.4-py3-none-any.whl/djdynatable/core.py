import contextlib
import importlib
from dataclasses import dataclass
from functools import wraps
from importlib import import_module, reload
from typing import Dict, List, Optional, Type

from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.db import ProgrammingError, connections, models
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import QuerySet
from django.utils.asyncio import async_unsafe
from rest_framework import serializers
from .handler import DynamicTableQueryHandler
from .exception import BaseException, TableDoesntExistException
from .utils import schema_aware, check_dependencies
from .models import (
    DEFAULT_FIELD_TYPES,
    DEFAULT_MODEL_ATTRS,
    RELATIONSHIP_FIELD,
    SchemaModel,
    Generated_model_objects,
)
from .compat import BASE_SCHEMA_NAME, DJANGO_PROJECT_NAME


try:
    from django_tenants.utils import schema_context
except Exception:
    pass
""" POTENTIAL WARNING :
    mixed migration and schema model can mingle ,
    never ever use create_model for this below method ,
    causes migrations loss and db clash
"""


""""default schema set as tables_ """


def install(model):
    from django.core.management import color, sql
    from django.db import connection

    style = color.no_style()

    cursor = connection.cursor()
    statements, pending = sql.sql_model_create(model, style)
    for sql in statements:
        cursor.execute(sql)


@dataclass
class DynamicTable:

    data: Dict
    new_table: bool = False
    model_cls: Optional[Type[models.Model]] = models.Model
    db_conn: Optional[None] = None
    schema_name: Optional[str] = None

    # def __new__(cls, data: Dict, new_table: bool = True):
    #     return super().__new__(cls)

    def __post_init__(self) -> None:
        self.model_cls: object = self.get_model_cls(self.data)
        self.db_conn: BaseDatabaseWrapper = connections["default"]
        if self.new_table:
            self.create_table()
        if self.schema_name is None:
            print("the schema name is ", self.schema_name)
            self.schema_name = BASE_SCHEMA_NAME

    @property
    def table_name(self) -> str:
        return self.model_cls._meta.db_table

    @property
    def table_verbose_name(self) -> str:
        return self.model_cls._meta.verbose_name

    @staticmethod
    def clear_all_objects() -> None:
        return Generated_model_objects.clear()

    def clear_object(self) -> None:
        return Generated_model_objects.pop(self.table_verbose_name)

    @schema_aware(lambda self: self.schema_name)
    @property
    def table_exists(
        self,
    ) -> bool:
        """checks if table exists in database"""
        return bool(
            [
                table
                for table in self.db_conn.introspection.table_names()
                if self.data["tblname"] in table
            ]
        )

    @classmethod
    def load_table_schema(cls, tblname: str, schema_name: str = None) -> "DynamicTable":

        def get_dynamic_table():
            schema_model = SchemaModel.objects.filter(table_name=tblname)
            if schema_model.exists():
                model_instance = schema_model.first()
                return cls(
                    {
                        "tblname": model_instance.table_name,
                        "columns": model_instance.columns,
                    },
                    new_table=False,
                    schema_name=schema_name,
                )
            raise TableDoesntExistException(
                code="table_doesnt_exist",
                detail=f"Table {tblname} does not exist.",
            )

        if check_dependencies() and schema_name:
            with schema_context(schema_name):
                return get_dynamic_table()

        return get_dynamic_table()

    @staticmethod
    def unregister_app(app_label, model_name) -> None:
        with contextlib.suppress(LookupError):
            app_config = apps.get_app_config(app_label)
            app_config.models_module = None
            app_config.import_models()

    def serialize_model_class(self, model_class):
        module_name = model_class.__module__
        class_name = model_class.__name__
        return f"{module_name}.{class_name}"

    @schema_aware(lambda self: self.schema_name)
    def deserialize_model_class(self, model_class_string):
        module_name, class_name = model_class_string.rsplit(".", 1)
        module = importlib.import_module(module_name)
        return getattr(module, class_name)

    @staticmethod
    @schema_aware(lambda self: self.schema_name)
    def register_app() -> None:
        with contextlib.suppress(Exception):
            admin.site.register(DynamicTable.model_cls)
        reload(import_module(settings.ROOT_URLCONF))

    def handle_column_changes(
        self,
        coldef: Dict,
        serializer: serializers.Serializer,
    ) -> None:
        table_query = DynamicTableQueryHandler(
            data=self.data, model_cls=self.model_cls, schema_name=self.schema_name
        )
        change_actions = {
            "add": table_query.add_column,
            "remove": table_query.remove_column,
            "alter": table_query.alter_column,
            "rename_table": lambda data: table_query.rename_db_table(
                old_table_name=self.table_name, new_table_name=data["new_table_name"]
            ),
        }

        change_type = coldef["change"]
        if change_type in change_actions:
            change_actions[change_type](serializer.data)
        else:
            raise ValueError(f"Unsupported change type: {change_type}")

    @schema_aware(lambda self: self.schema_name)
    def get_model_cls(self, data: Dict) -> models.Model:

        # if Generated_model_objects.get(str(data["tblname"])):
        #     return Generated_model_objects[str(data["tblname"])]

        class Meta:
            app_label = "tables"
            verbose_name = data["tblname"]
            verbose_name_plural = data["tblname"]
            db_table = "tables_" + data["tblname"]

        model_attrs = {
            "__module__": models.Model.__module__,
            "app_label": f"{DJANGO_PROJECT_NAME}.tables",
            "Meta": Meta,
        }

        for col_dict in data["columns"]:
            model_attrs[col_dict["colname"]] = DEFAULT_FIELD_TYPES[col_dict["coltype"]](
                **DEFAULT_MODEL_ATTRS[col_dict["coltype"]]
            )
            if col_dict["coltype"] in RELATIONSHIP_FIELD:
                model_attrs[col_dict["colname"]].db_column = col_dict["colname"]
                model_attrs[col_dict["colname"]].related_query_name = col_dict[
                    "colname"
                ]
                model_attrs[col_dict["colname"]].related_name = col_dict["colname"]

        model_klass = type(data["tblname"], (models.Model,), model_attrs)

        Generated_model_objects[data["tblname"]] = model_klass

        return model_klass

    @schema_aware(lambda self: self.schema_name)
    def create_table(self) -> None:
        try:
            with self.db_conn.schema_editor() as schema_editor:
                schema_editor.create_model(self.model_cls)
        except ProgrammingError as e:
            tblexc = BaseException(
                code="table_create_error",
                detail=f"Error while creating table: '{self.data['tblname']}.'",
            )
            tblexc.status_code = 400
            raise tblexc from e
        else:
            schema_model_obj = SchemaModel(
                table_name=self.data["tblname"], columns=self.data["columns"]
            )
            schema_model_obj.save()

    def get_fields(self) -> List:
        return [x["colname"] for x in self.data["columns"]]

    def get_fields_with_types(self) -> List:
        return [
            DEFAULT_FIELD_TYPES[x["coltype"]](DEFAULT_MODEL_ATTRS[x["coltype"]])
            for x in self.data["columns"]
        ]

    def get_serializer(self) -> serializers.ModelSerializer:
        """creates Dynamic Table Serializer class from model class"""
        meta_cls = type(
            "Meta",
            (object,),
            {
                "model": self.model_cls,
                "fields": self.get_fields(),
            },
        )
        return type(
            "DynamicTableSerializer", (serializers.ModelSerializer,), {"Meta": meta_cls}
        )

    @schema_aware(lambda self: self.schema_name)
    def drop_table(self) -> None:
        """drops the table from database"""
        try:
            with self.db_conn.schema_editor() as schema_editor:
                schema_editor.delete_model(self.model_cls)
            with contextlib.suppress(Exception) as e:
                Generated_model_objects.pop(self.data["tblname"])
        except ProgrammingError as e:
            BaseException(
                code="table_delete_error",
                detail=f"Table {self.data['table_name']} does not exists.",
            )
        else:
            # self.unregister_app(self.data["tblname"], self.data["tblname"])
            SchemaModel.objects.filter(table_name=self.data["tblname"]).delete()

    @schema_aware(lambda self: self.schema_name)
    def get_queryset(self) -> QuerySet:
        return self.model_cls.objects.all()

    def __delattr__(self, name: str) -> None:
        pass  # noqa
        # self.drop_table()

    def auto_commit(f):
        @wraps(f)
        @async_unsafe
        def wrapper(*args, **kwds):
            return f(*args, **kwds)

        return wrapper
