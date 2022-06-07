from rest_framework.views import APIView, Response, status, Request
from suconnect_1.metadata import CustomMetadata
from suconnect_1.pagination import CustomPagination


class BaseListView(APIView, CustomPagination):
    
    name = "Base list view"
    description = "This is the base list view."

    authentication_classes = []
    permission_classes = []

    metadata_class = CustomMetadata

    related_fields = []


    def _send_metadata(self, request):

        data = self.metadata_class().determine_metadata(request, self)

        return Response(
            {
                "isError":False,
                "message": "metadata",
                "data": data
            }
        )



    def get(self, request: Request):
        
        # if meta query_param is present, return metadata of the current endpoint
        if request.GET.get("meta"):
            return self._send_metadata(request)

        # make a query from the database
        queryset = self.model.objects.prefetch_related(
            *self.related_fields
            ).all()

        # paginate the queryset
        paginated_data = self.paginate_queryset(
            queryset, request
        )
        
        # serialize the paginated queryset
        serialized_data = self.serializer(
            paginated_data,
            many=True,

        )

        # return the serialized queryset in a standardized manner
        return self.get_paginated_response({
            "isError": False,
            "message": "success",
            "data": serialized_data.data
        }, status=status.HTTP_200_OK)
        