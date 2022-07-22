from rest_framework.views import APIView, Response, status, Request
from schedjuice5.metadata import CustomMetadata
from schedjuice5.pagination import CustomPagination
from schedjuice5.renderer import CustomRenderer
from rest_framework.renderers import BrowsableAPIRenderer


class BaseView(APIView):
    name = "Base view (not cringe view)"

    authentication_classes = []
    permission_classes = []

    # customizing the response format
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    @staticmethod
    def send_response(is_error: bool, message: str, data, **kwargs) -> Response:
        return Response(
            {"isError": is_error, "message": message, "data": data}, **kwargs
        )


class BaseListView(BaseView, CustomPagination):

    name = "Base list view"

    metadata_class = CustomMetadata

    related_fields = []

    def _send_metadata(self, request: Request):

        data = self.metadata_class().determine_metadata(request, self)

        return self.send_response(False, "metadata", data, status=status.HTTP_200_OK)

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
        serialized_data = self.serializer(
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

        serialized_data = self.serializer(
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
