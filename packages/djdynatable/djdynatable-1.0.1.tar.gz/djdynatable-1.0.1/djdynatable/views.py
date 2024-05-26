from django.shortcuts import get_object_or_404
from djeasyview.response import FailureResponse, SuccessResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import contextlib
from .core import DynamicTable
from .models import DEFAULT_MODEL_ATTRS, SchemaModel
from .serializer import ColumnChangeSerializer, TableSerializer
from .utils import schema_aware, BaseDispath


class TableListCreateApiView(BaseDispath, APIView):
    queryset = None
    serializer_class = TableSerializer
    permission_classes = [AllowAny]

    @schema_aware(lambda self: self.schema_name)
    def base_queryset(self, table_name):
        schema_table = get_object_or_404(SchemaModel, table_name=table_name)
        columns = ["id"] + [x["colname"] for x in schema_table.columns]
        try:
            table = DynamicTable.load_table_schema(
                table_name, schema_name=str(self.schema_name)
            )
        except Exception:
            table = DynamicTable.load_table_schema(
                table_name, schema_name=str(self.schema_name)
            ).clear_all_objects()

        return schema_table, table, columns

    @schema_aware(lambda self: self.schema_name)
    def get(self, request):
        with contextlib.suppress(Exception):
            table_name = self.request.query_params.get("table_name")
            table = DynamicTable.load_table_schema(
                tblname=table_name, schema_name=self.schema_name
            )

            schema_table, table, columns = self.base_queryset(table_name)
            if schema_table:
                rows = table.get_queryset().values(*columns).order_by("id")
                return SuccessResponse(
                    {
                        "columns": schema_table.columns,
                        "rows": (list(rows)),
                    }
                )
            return SuccessResponse([])
        return FailureResponse("Matching data not found")

    @schema_aware(lambda self: self.schema_name)
    def post(self, request):
        """for table creation"""
        table_serializer = TableSerializer(data=request.data)
        if table_serializer.is_valid():
            DynamicTable(
                table_serializer.data,
                new_table=True,
                schema_name=self.schema_name,
            )
            return SuccessResponse(table_serializer.data)
        return FailureResponse(table_serializer.errors, status=400)


class TableUpdateDeleteApiView(BaseDispath, APIView):
    queryset = None
    serializer_class = TableSerializer
    permission_classes = [AllowAny]

    @schema_aware(lambda self: self.schema_name)
    def put(self, request, table_name):
        body_data = JSONParser().parse(request)
        serializer = ColumnChangeSerializer(data=body_data)
        if serializer.is_valid():
            table = DynamicTable.load_table_schema(
                table_name, schema_name=self.schema_name
            )
            if table.table_exists:
                table.clear_object()
                table.handle_column_changes(coldef=body_data, serializer=serializer)
                return SuccessResponse("Data updated successfully")
            return FailureResponse(f"Table {table_name} does not exists")
        return Response("Something went wrong", status=status.HTTP_400_BAD_REQUEST)

    @schema_aware(lambda self: self.schema_name)
    def delete(self, request, table_name):
        table = DynamicTable.load_table_schema(table_name, schema_name=self.schema_name)
        if table.table_exists:
            table.drop_table()
            return SuccessResponse(f"table {table_name} deleted successfully")
        return FailureResponse(f"table {table_name} does not exists")


class RowListCreateUpdateDeleteApiView(BaseDispath, APIView):
    queryset = None
    permission_classes = [AllowAny]

    @schema_aware(lambda self: self.schema_name)
    def post(self, request, table_name):
        table = DynamicTable.load_table_schema(table_name, schema_name=self.schema_name)
        if any(value == "" for value in request.data.values()):
            table.model_cls.objects.create()
            return SuccessResponse("row created successfully")
        table_serializer = table.get_serializer()(data=request.data)
        if table_serializer.is_valid():
            table_serializer.save()
            return SuccessResponse(table_serializer.data)
        return FailureResponse(table_serializer.errors)

    @schema_aware(lambda self: self.schema_name)
    def get(self, request, table_name):
        table = DynamicTable.load_table_schema(table_name, schema_name=self.schema_name)
        rows = table.model_cls.objects.all()
        return Response({"rows": list(rows.values())})

    @schema_aware(lambda self: self.schema_name)
    def put(self, request, table_name):
        body_data = request.data
        table = DynamicTable.load_table_schema(table_name, schema_name=self.schema_name)
        queryset = table.get_queryset()
        if any(value is None or value == "" for value in body_data.values()):
            qryst = queryset.filter(id=body_data["id"])
            body_data.pop("id")
            qryst.update(**body_data)
            return SuccessResponse("row updated successfully")
        serializer = table.get_serializer()(
            instance=queryset.get(id=body_data["id"]), data=body_data
        )
        if serializer.is_valid():
            serializer.update(
                instance=serializer.instance, validated_data=serializer.validated_data
            )
            return SuccessResponse(serializer.data)
        return FailureResponse(serializer.errors)

    @schema_aware(lambda self: self.schema_name)
    def delete(self, request, table_name):
        row_id = self.request.query_params.get("id")
        table = DynamicTable.load_table_schema(
            table_name,
            schema_name=self.schema_name,
        )
        if table.table_exists:
            queryset = table.get_queryset().filter(id=row_id)
            if queryset.exists():
                queryset.delete()
                return SuccessResponse(f"row  {row_id} deleted successfully")
            return FailureResponse("matching row not found")
        return FailureResponse(f"table {table_name} does not exists")


class FieldListApiview(APIView):
    queryset = None
    serializer_class = None
    permission_classes = [AllowAny]

    def get(self, request):
        return SuccessResponse(DEFAULT_MODEL_ATTRS.keys())
