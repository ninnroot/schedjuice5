from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):

        fields = kwargs.pop("fields", None)
        read_only_fields = kwargs.pop("read_only_fields", None)
        excluded_fields = kwargs.pop("excluded_fields", None)

        if fields:
            fields = fields.split(",")

        super(BaseModelSerializer, self).__init__(*args, **kwargs)

    class Meta:
        fields = "__all__"


class BaseSerializer(serializers.Serializer):
    pass
