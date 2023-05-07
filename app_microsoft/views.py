from django.shortcuts import render
from utilitas.views import BaseView


class TestView(BaseView):
    def get(self, request):
        x = get_token()
        print(x)
        return self.send_response(False, "ok", {})
