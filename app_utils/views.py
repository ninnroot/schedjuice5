from schedjuice5.views import BaseView
from .choices import careers, countries


class CountryView(BaseView):
    name = "Country view"
    choices = countries

    def get(self, request):
        return self.send_response(
            False, "success", {"data": {"countries": self.choices}}
        )


class CareerView(BaseView):
    name = "Career view"
    choices = careers

    def get(self, request):
        return self.send_response(False, "success", {"data": {"careers": self.choices}})
