from schedjuice5.views import BaseView
from .choices.country_codes import country_codes
from .choices.careers import careers
from .choices.postal_codes import postal_codes
from .choices.dial_codes import dial_codes


class CountryView(BaseView):
    name = "Country view"
    choices = country_codes

    def get(self, request):
        return self.send_response(
            False, "success", {"data": {"countries": self.choices}}
        )


class CareerView(BaseView):
    name = "Career view"
    choices = careers

    def get(self, request):
        return self.send_response(False, "success", {"data": {"careers": self.choices}})


class DialCodeView(BaseView):
    name = "Dial code view"
    choices = dial_codes

    def get(self, request):
        return self.send_response(False, "success", {"data": {"dial_codes": self.choices}})


class PostalCodeView(BaseView):
    name = "Postal code view"
    choices = postal_codes

    def formatData(self, data):
        return {
            "name": data[0],
            "township": data[1],
            "region": data[2],
            "postal_code": data[3],
        }

    def get(self, request, postal_code=None):
        print(postal_code)
        if postal_code is not None:
            for row in self.choices:
                if row[3] == postal_code:
                    return self.send_response(False, "success", {"data": self.formatData(row)})
            return self.send_response(True, "error", {"message": "Postal code not found"})
        else: 
            return self.send_response(
                False, "success", {"data": {"postal_codes": self.choices}}
            )
