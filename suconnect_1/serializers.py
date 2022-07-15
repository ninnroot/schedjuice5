from rest_framework.serializers import Serializer


class BaseSerializer(Serializer):
    def __init__(self, *args, **kwargs):

        fields = kwargs.pop("fields", None)
        read_only_fields = kwargs.pop("read_only_fields", None)
        excluded_fields = kwargs.pop("excluded_fields", None)

        if fields:
            fields = fields.split(",")

        super(BaseSerializer, self).__init__(*args, **kwargs)
