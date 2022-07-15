from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        data["foo"] = "bar"

        return super(CustomRenderer, self).render(
            data, accepted_media_type, renderer_context
        )
