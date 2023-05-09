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
        res = ms_user.create(
            request.data["display_name"],
            request.data["principal_name"],
            request.data["password"],
        )
        user_id = res.json()["id"]
        email = res.json()["userPrincipalName"]
        ms_user.enable_mail(user_id, email)
        res = ms_user.assign_license(user_id, "staff")
        print(res.json())
        return self.send_response(
            False,
            "err...idk ",
            res.json(),
        )
