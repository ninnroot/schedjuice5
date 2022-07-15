from rest_framework.schemas.generators import EndpointEnumerator
from rest_framework.views import Response
from suconnect_1.views import BaseView
from suconnect_1.utils import send_response


class DocView(BaseView):
    name = "Endpoint listing"
    description = "This is the listing of all the endpoints of the SuConnect API."

    def get(self, request):
        lst = sorted(
            [
                {
                    "method": i[1],
                    "url": i[0],
                }
                for i in EndpointEnumerator().get_api_endpoints()
            ],
            key=lambda x: x["url"],
        )

        return send_response(False, self.description, lst, status=200)
