from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# customizing the PageNumberPagination class to my liking.


class CustomPagination(PageNumberPagination):

    page_size_query_param = "size"

    def get_paginated_response(self, response, status):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                **response,
            },
            status=status,
        )
