from django.shortcuts import render
from rest_framework.views import Request, Response
from utilitas.views import BaseView

from app_microsoft.graph_wrapper.user import MSUser


class TestView(BaseView):
    def get(self, request: Request):
        user_id = request.query_params.get("user_id")

        ms_user = MSUser()

        return self.send_response(False, "ok", ms_user.get(user_id).json())

    def post(self, request: Request):
        ms_user = MSUser()
        respond = ms_user.create(
            request.data["display_name"],
            request.data["principal_name"],
            request.data["password"],
        )
        return self.send_response(
            respond.status_code not in range(199, 300),
            "err...idk ",
            respond.json(),
            status=respond.status_code,
        )
