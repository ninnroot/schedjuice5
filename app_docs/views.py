from rest_framework.schemas.generators import EndpointEnumerator
from rest_framework.views import APIView, Response


class DocView(APIView):
    def get(self, request):
        lst = EndpointEnumerator().get_api_endpoints()
        for i in lst:
            print(i)
        return Response({"data": ""})
