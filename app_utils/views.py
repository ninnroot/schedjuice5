from schedjuice5.views import BaseView
from .choices import carrers, countries

class CountryView(BaseView):
    name = "Country view"
    choices = countries

    def get(self, request):
        return self.send_response(False, "success", {"countries": self.choices})


class CarrerView(BaseView):
    name = "Carrer view"
    choices = carrers

    def get(self, request):
        return self.send_response(False, "success", {"careers": self.choices})