from schedjuice5.views import BaseDetailsView, BaseListView, BaseSearchView

from .models import *
from .serializers import *

# ------------ Assignment Section ------------
class AssignmentListView(BaseListView):
    name = "Assignment list view"
    model = Assignment
    serializer = AssignmentSerializer


class AssignmentDetailsView(BaseDetailsView):
    name = "Assignment details view"
    model = Assignment
    serializer = AssignmentSerializer


class AssignmentSearchView(BaseSearchView):
    name = "Assignment search view"
    model = Assignment
    serializer = AssignmentSerializer
    
    
# ------------ Attachment Section ------------
class AttachmentListView(BaseListView):
    name = "Attachment list view"
    model = Attachment
    serializer = AttachmentSerializer


class AttachmentDetailsView(BaseDetailsView):
    name = "Attachment details view"
    model = Attachment
    serializer = AttachmentSerializer


class AttachmentSearchView(BaseSearchView):
    name = "Attachment search view"
    model = Attachment
    serializer = AttachmentSerializer
    
    
# ------------ Submission Section ------------
class SubmissionListView(BaseListView):
    name = "Submission list view"
    model = Submission
    serializer = SubmissionSerializer


class SubmissionDetailsView(BaseDetailsView):
    name = "Submission details view"
    model = Submission
    serializer = SubmissionSerializer


class SubmissionSearchView(BaseSearchView):
    name = "Submission search view"
    model = Submission
    serializer = SubmissionSerializer
    
    
# ------------ SubmissionAttachment Section ------------
class SubmissionAttachmentListView(BaseListView):
    name = "SubmissionAttachment list view"
    model = SubmissionAttachment
    serializer = SubmissionAttachmentSerializer


class SubmissionAttachmentDetailsView(BaseDetailsView):
    name = "SubmissionAttachment details view"
    model = SubmissionAttachment
    serializer = SubmissionAttachmentSerializer


class SubmissionAttachmentSearchView(BaseSearchView):
    name = "SubmissionAttachment search view"
    model = SubmissionAttachment
    serializer = SubmissionAttachmentSerializer


"""
{
    "fullMark": 100,
    "passMark": 40,
    "criteria": [
        {
            "name": "A",
            "description": "distinction",
            "range": 80
        },
        {
            "name": "B",
            "description": "pass",
            "range": 60
        },
        {
            "name": "C",
            "description": "pass",
            "range": 40
        },
        {
            "name": "D",
            "description": "fail",
            "range": 0
        }
    ]
}
"""