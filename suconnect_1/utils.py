from rest_framework.views import Response


def send_response(is_error: bool, message: str, data, **kwargs) -> Response:
    return Response({"isError": is_error, "message": message, "data": data}, **kwargs)
