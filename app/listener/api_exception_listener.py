from rest_framework.views import exception_handler as rest_framework_exception_handler


def exception_handler(exc, context):
    response = rest_framework_exception_handler(exc, context)

    if response is not None:
        response.data["status_code"] = response.status_code

    return response
