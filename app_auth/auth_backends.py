from rest_framework_simplejwt.authentication import JWTAuthentication

# Code is currently unused

# class CustomBackend:
#     authenticator = JWTAuthentication()

#     def authenticate(self, request=None, **kwargs):

#         if request is None:
#             return None
#         tuple_user = self.authenticator.authenticate(request)

#         if type(tuple_user) is tuple:
#             return tuple_user[0]

#         return None
