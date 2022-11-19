import base64
import json

from django.core.exceptions import BadRequest
from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.views import APIView, Request, Response, status

from schedjuice5.metadata import CustomMetadata
from schedjuice5.pagination import CustomPagination
from schedjuice5.renderer import CustomRenderer
from schedjuice5.serializers import FilterParamSerializer
from schedjuice5.swagger_serializers import FilterParamsSerializer
from schedjuice5.swagger_query_params import *



class BaseView(APIView, CustomPagination):
    name = "Base view (not cringe view)"
    description = ""

    authentication_classes = []
    permission_classes = []
    model = None
    serializer = None

    # customizing the response format
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    related_fields = []

    # sending metadata
    def send_metadata(self, request: Request):
        if not hasattr(self, "metadata_class"):
            return self.get(request)
        data = self.metadata_class().determine_metadata(request, self)

        return self.send_response(
            False, "metadata", {"data": data}, status=status.HTTP_200_OK
        )

    # querying data
    def get_queryset(
        self, request: Request, filter_params=None, exclude_params={}, fields=None, sorts=None, expand=None
    ):
        if filter_params is None:
            filter_params = {}

        if fields is None:
            fields = []

        if expand is None:
            expand = []
        # query from the database
        queryset = (
            self.model.objects.filter(**filter_params).exclude(**exclude_params)
            .prefetch_related(*self.related_fields)
            .all()
            .order_by(*sorts)
        )

        # paginate the queryset
        paginated_data = self.paginate_queryset(queryset, request)

        # serialize the paginated data
        serialized_data = self.get_serializer(
            paginated_data,
            many=True,
            fields=fields,
            expand=expand,
            context={"model": self.model},
        )

        return serialized_data

    # make sure the fields are actually present in the model
    def fields_are_valid(self, fields: list) -> bool:
        return set(fields).issubset(self.model.get_filterable_fields(self.model))

    # get the "field" parameter form the request's body
    def get_field_filter_param(self, request: Request):
        fields = []
        x = request.query_params.get("fields")
        if x:
            fields = self.decode_query_param(x, "fields")
            # if not self.fields_are_valid(fields):
            #     raise BadRequest(
            #         f"{set(fields).difference(self.model.get_filterable_fields(self.model))}"
            #         f" are not present in {self.model.__name__}'s field set"
            #     )

        return fields

    # get the "sort" query param
    def get_sort_param(self, request: Request):
        sorts = request.query_params.get("sorts", [])  # get base64 encoded string
        if sorts:
            sorts = self.decode_query_param(sorts, "sorts")  # decode base64 string
            rmv_sign_sort = [sort.replace("-", "") for sort in sorts]
            if not self.fields_are_valid(rmv_sign_sort):
                raise BadRequest(
                    f"{sorts} is not present in {self.model.__name__}'s sortable fields"
                )

        return sorts

    # get the "expand" parameter from the request's body
    def get_expand_param(self, request: Request):
        expand = request.query_params.get("expand", [])
        if expand:
            expand = self.decode_query_param(expand, "expand")

        return expand

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
        return self.serializer

    def get_serializer_context(self):
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    @staticmethod
    def send_response(is_error: bool, message: str, payload, **kwargs) -> Response:
        return Response({"isError": is_error, "message": message, **payload}, **kwargs)

    @staticmethod
    def decode_query_param(url_string: str, param_name: str):
        try:
            param = json.loads(
                base64.urlsafe_b64decode(url_string + "=" * (4 - len(url_string) % 4))
            )
        except Exception as e:
            raise BadRequest(f"Error decoding {param_name}: " + str(e))

        return param


class BaseListView(BaseView):

    name = "Base list view"
    metadata_class = CustomMetadata

    @swagger_auto_schema(
        manual_parameters=[size_param, page_param, sorts_param, fields_param, expand_param]
    )
    def get(self, request: Request):
        self.description = self.model.__doc__

        # if meta query_param is present, return metadata of the current endpoint
        if request.GET.get("meta"):
            return self.send_metadata(request)

        sorts = []
        try:
            sorts = self.get_sort_param(request)
            expand = self.get_expand_param(request)
            fields = self.get_field_filter_param(request)
        except BadRequest as e:
            return self.send_response(
                True, "bad_request", {"details": str(e)}, status=400
            )

        serialized_data = self.get_queryset(
            request, sorts=sorts, expand=expand, fields=fields
        )

        # return the serialized queryset in a standardized manner
        return self.send_response(
            False,
            "success",
            {**self.get_paginated_response(), "data": serialized_data.data},
            status=status.HTTP_200_OK,
        )

    # create
    def post(self, request: Request):

        serialized_data = self.get_serializer(
            data=request.data,
        )
        if serialized_data.is_valid():
            serialized_data.save()
            return self.send_response(
                False,
                "created",
                {"data": serialized_data.data},
                status=status.HTTP_201_CREATED,
            )

        return self.send_response(
            True,
            "bad_request",
            {"details": serialized_data.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class BaseDetailsView(BaseView):
    name = "Base details view"
    metadata_class = CustomMetadata

    def _get_object(self, obj_id: int):
        obj = self.model.objects.filter(id=obj_id).first()
        return obj

    def _send_not_found(self, obj_id: int):
        return self.send_response(
            True,
            "not_found",
            {"details": f"{str(self.model)} with id {obj_id} does not exist."},
            status=status.HTTP_404_NOT_FOUND,
        )

    # get-one
    @swagger_auto_schema(
        manual_parameters=[fields_param, expand_param]
    )
    def get(self, request: Request, obj_id: int):
        self.description = self.model.__doc__

        fields = self.get_field_filter_param(request)
        expand = self.get_expand_param(request)

        obj = self._get_object(obj_id)
        if obj is None:
            return self._send_not_found(obj_id)
        serialized_data = self.get_serializer(obj, expand=expand, fields=fields)
        return self.send_response(
            False, "success", {"data": serialized_data.data}, status=status.HTTP_200_OK
        )

    # update
    def put(self, request: Request, obj_id: int):
        obj = self._get_object(obj_id)
        if obj is None:
            return self._send_not_found(obj_id)
        serialized_data = self.get_serializer(obj, data=request.data, partial=True)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return self.send_response(
            False, "updated", {"data": serialized_data.data}, status=status.HTTP_200_OK
        )

    def delete(self, request: Request, obj_id: int):
        obj = self._get_object(obj_id)
        if obj is None:
            return self._send_not_found(obj_id)
        serialized_data = self.get_serializer(obj)
        obj.delete()
        return self.send_response(
            False, "deleted", {"data": serialized_data.data}, status=status.HTTP_200_OK
        )


class BaseSearchView(BaseView):
    name = "Base search view"

    # making sure the filter_params object is valid
    def validate_body_params(self, to_be_validated):
        validated_data = []
        for i in to_be_validated:
            x = FilterParamSerializer(data=i, context={"model": self.model})
            if not x.is_valid(raise_exception=True):
                raise BadRequest(x.errors)
            validated_data.append(x.data)

        return validated_data

    # building a filter_params dict to be used in querying
    @staticmethod
    def build_body_params(body_params):
        params_dict = {}
        for i in body_params:
            params_dict[i["field_name"] + "__" + i["operator"]] = (
                i["value"].split(",") if i["operator"] == "in" else i["value"]
            )

        return params_dict

    # get filter_params from the request
    def get_filter_params(self, request: Request):
        filter_params = request.data.get("filter_params", {})
        validated_filter_params = self.validate_body_params(filter_params)
        return self.build_body_params(validated_filter_params)
    
    # get exclude_params from the request
    def get_exclude_params(self, request: Request):
        exclude_params = request.data.get("exclude_params", {})
        validated_exclude_params = self.validate_body_params(exclude_params)
        return self.build_body_params(validated_exclude_params)

    # search
    @swagger_auto_schema(
        request_body=FilterParamsSerializer,
        manual_parameters=[size_param, page_param, sorts_param, fields_param, expand_param],
    )
    def post(self, request: Request):

        filter_params = {}
        try:
            fields = self.get_field_filter_param(request)
            filter_params = self.get_filter_params(request)
            exclude_params = self.get_exclude_params(request)
            sorts = self.get_sort_param(request)
            expand = self.get_expand_param(request)
        except BadRequest as e:
            return self.send_response(
                True, "bad_request", {"details": str(e)}, status=400
            )

        serialized_data = self.get_queryset(
            request, filter_params, exclude_params, fields, sorts, expand
        )

        # return the serialized queryset in a standardized manner
        return self.send_response(
            False,
            "success",
            {**self.get_paginated_response(), "data": serialized_data.data},
            status=status.HTTP_200_OK,
        )
