from schedjuice5.serializers import BaseModelSerializer

from .models import *


class AnnouncementSerializer(BaseModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"

    expandable_fields = {
                            "created_by": "app_users.serializers.StaffSerializer",
                            "attachment_set": ("app_announcement.serializers.AttachmentSerializer", {"many": True})
                        }
    
    
class AttachmentSerializer(BaseModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"

    expandable_fields = {"announcement": "app_announcement.serializers.AnnouncementSerializer"}
