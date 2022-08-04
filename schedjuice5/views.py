from rest_framework.views import APIView, Response, status, Request
from rest_framework.renderers import BrowsableAPIRenderer

from schedjuice5.metadata import CustomMetadata
from schedjuice5.pagination import CustomPagination
from schedjuice5.renderer import CustomRenderer

class BaseView(APIView):
    name = "Base view (not cringe view)"

    authentication_classes = []
    permission_classes = []

    # customizing the response format
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    serailizer = None

    def get_serializer(self, *args, **kwargs):
        serializer = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer(*args, **kwargs)

    def get_serializer_class(self):
        return self.serializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    @staticmethod
    def send_response(is_error: bool, message: str, data, **kwargs) -> Response:
        return Response(
            {"isError": is_error, "message": message, "data": data}, **kwargs
        )

    def _send_metadata(self, request: Request):
        if not hasattr(self, "metadata_class"):
            return self.get(request)
        data = self.metadata_class().determine_metadata(request, self)

        return self.send_response(False, "metadata", data, status=status.HTTP_200_OK)


class BaseListView(BaseView, CustomPagination):

    name = "Base list view"
    metadata_class = CustomMetadata
    related_fields = []

    def get(self, request: Request):

        self.description = self.model.__doc__

        # if meta query_param is present, return metadata of the current endpoint
        if request.GET.get("meta"):
            return self._send_metadata(request)

        # make a query from the database
        queryset = self.model.objects.prefetch_related(*self.related_fields).all()

        # paginate the queryset
        paginated_data = self.paginate_queryset(queryset, request)

        # serialize the paginated queryset
        serialized_data = self.get_serializer(
            paginated_data,
            many=True,
        )

        # return the serialized queryset in a standardized manner
        return self.send_response(
            False,
            "success",
            {**self.get_paginated_response(), "data": serialized_data.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request):

        serialized_data = self.get_serializer(
            data=request.data,
        )
        if serialized_data.is_valid():
            serialized_data.save()
            return self.send_response(
                False, "created", serialized_data.data, status=status.HTTP_201_CREATED
            )

        return self.send_response(
            True,
            "bad_request",
            serialized_data.errors,
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

    def get(self, request: Request, obj_id: int):
        self.description = self.model.__doc__
        obj = self._get_object(obj_id)
        if obj is None:
            return self._send_not_found(obj_id)
        serialized_data = self.get_serializer(obj)
        return self.send_response(
            False, "success", serialized_data.data, status=status.HTTP_200_OK
        )

    def put(self, request: Request, obj_id: int):
        obj = self._get_object(obj_id)
        if obj is None:
            return self._send_not_found(obj_id)
        serialized_data = self.get_serializer(obj, data=request.data, partial=True)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return self.send_response(
            False, "updated", serialized_data.data, status=status.HTTP_200_OK
        )

    def delete(self, request: Request, obj_id: int):
        obj = self._get_object(obj_id)
        if obj is None:
            return self._send_not_found(obj_id)
        serialized_data = self.get_serializer(obj)
        obj.delete()
        return self.send_response(
            False, "deleted", serialized_data.data, status=status.HTTP_200_OK
        )
