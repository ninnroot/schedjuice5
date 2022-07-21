from schedjuice5.serializers import BaseSerializer
from app_auth.models import Account


class AccountSerializer(BaseSerializer):
    class Meta:
        model = Account
        fields = "__all__"

    def create(self, validated_data):

        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user
