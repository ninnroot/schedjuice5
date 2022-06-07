from rest_framework.views import APIView, Response, status


class BaseListView(APIView):
    
    name = "Base list view"
    description = "This is the base list view."

    authentication_classes = []
    permission_classes = []


    def get(self, request):
        
        serialized_data = self.serializer(
            self.model.objects.all(),
            many=True,

        )

        return Response({
            "message": "success",
            "data":serialized_data.data
        })
        