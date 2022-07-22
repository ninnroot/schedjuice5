from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate


class CustomBackend:
    authenticator = JWTAuthentication()

    def authenticate(self, request=None, **kwargs):
        if request is None:
            return None
        print("I ran")
        tuple_user = self.authenticator.authenticate(request)

        if type(tuple_user) is tuple:
            return tuple_user[0]

        return None
