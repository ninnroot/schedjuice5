
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated

class Test(APIView):
    permission_classes = []
    def get(self, request):

        print(request.user)
        
        return Response({"message": "hello world"})
