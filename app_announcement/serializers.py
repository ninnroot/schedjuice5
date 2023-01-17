from schedjuice5.serializers import BaseModelSerializer

from .models import *


class AnnouncementSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Announcement
        fields = "__all__"

    expandable_fields = {
        "created_by": "app_users.serializers.StaffSerializer",
        "attachments": (
            "app_announcement.serializers.AttachmentSerializer",
            {"many": True},
        ),
    }


class AttachmentSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Attachment
        fields = "__all__"

    expandable_fields = {
        "announcement": "app_announcement.serializers.AnnouncementSerializer"
    }
