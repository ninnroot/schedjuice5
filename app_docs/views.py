from rest_framework.schemas.generators import EndpointEnumerator
from rest_framework.views import Response

from schedjuice5.views import BaseView


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

        return self.send_response(False, self.description, lst, status=200)
