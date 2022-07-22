from rest_framework.views import exception_handler


def custom_handler(exc, ctx):
    response = exception_handler(exc, ctx)
    if hasattr(exc, "status_code") and exc.status_code in [401, 403]:
        response.data["isError"] = True

    return response
