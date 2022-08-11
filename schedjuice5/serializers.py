from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        read_only_fields = kwargs.pop("read_only_fields", None)
        excluded_fields = kwargs.pop("excluded_fields", None)
        super(BaseModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            fields_to_be_popped = set(
                self.context["model"].get_filterable_fields(self.context["model"])
            ).difference(fields)
            for i in fields_to_be_popped:
                try:
                    self.fields.pop(i)
                except KeyError:
                    pass


class BaseSerializer(serializers.Serializer):
    pass


class FilterParamSerializer(BaseSerializer):
    field_name = serializers.CharField(max_length=32, required=True)
    operator = serializers.CharField(max_length=16, default="exact")
    value = serializers.CharField(max_length=32, required=True)

    def validate(self, data, *args, **kwargs):
        if data["field_name"] not in self.context["model"].get_filterable_fields(
            self.context["model"]
        ):
            raise serializers.ValidationError(
                f"{data['field_name']} is not in the field set of {self.context['model'].__name__}"
            )

        if data["operator"] not in self.context["model"].valid_operators:
            raise serializers.ValidationError(
                f"{data['operator']} is not in valid operators of {self.context['model'].__name__}. "
                f"Valid operators: {self.context['model'].valid_operators}"
            )

        return data
