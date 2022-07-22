from rest_framework.views import exception_handler


def custom_handler(exc, ctx):
    response = exception_handler(exc, ctx)

    response.data["isError"] = True

    return response
