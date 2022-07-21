from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None, **kwargs):

        if "message" not in data.keys():
            data["message"] = ""

        if "isError" not in data.keys():

            data["isError"] = False
            if "message" not in data.keys():
                data["message"] = "Error not specified"

        return super(CustomRenderer, self).render(
            data, accepted_media_type, renderer_context
        )
