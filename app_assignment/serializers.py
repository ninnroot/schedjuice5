import base64
from rest_framework.serializers import ValidationError
from rest_framework import serializers
from schedjuice5.serializers import BaseModelSerializer, BaseSerializer

from .models import *


class CriteriaSerailizer(BaseSerializer):
    name = serializers.CharField(max_length=25, required=True)
    description = serializers.CharField(max_length=100, required=True)
    range = serializers.IntegerField()
    

class GradingCriteriaSerializer(BaseSerializer):
    fullMark = serializers.IntegerField()
    passMark = serializers.IntegerField()
    criteria = CriteriaSerailizer(many=True)
    
    def validate(self, attrs):
        if (attrs['passMark'] > attrs['fullMark']):
            raise ValidationError("FullMark must be greater than PassMark.")
        
        for criteria in attrs['criteria']:
            if not (-1 < criteria['range'] < attrs['fullMark'] + 1):
                raise ValidationError({"range": f"Range value must be between 0 and {attrs['fullMark']}"})
            
        return super().validate(attrs)


class AssignmentSerializer(BaseModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"
        
    expandable_fields = {
        "staff": ("app_users.serializers.StaffSerializer",),
        "submission_set": ("app_assignment.serializers.SubmissionSerializer", {"many": True},),
        "attachment_set": ("app_assignment.serializers.AttachmentSerializer", {"many": True},),
    }
    
    def update(self, instance, validated_data):
        # these are the attrs we can update after published.
        valid_attrs_to_update = ['name', 'instruction', 'is_published']
        
        if instance.is_first_published and instance.is_published:
            # filtering not_allow_attrs and allow_attrs from request data.
            not_allow_attrs = list(filter(lambda attr: attr not in valid_attrs_to_update, list(validated_data.keys())))
            allow_attrs = list(filter(lambda attr: attr in valid_attrs_to_update, list(validated_data.keys())))

            if len(not_allow_attrs) > 0:
                raise ValidationError(f"({', '.join(not_allow_attrs)}) {'attributes are' if len(not_allow_attrs) > 1 else 'attribute is'} not allowed to update after published.")
            else:
                for attr in allow_attrs:
                    setattr(instance, attr, validated_data.get(attr))

            instance.save()
            return instance
        
        return super().update(instance, validated_data)
    
    def save(self, **kwargs):
        # if the assignment is published, is_first_published attr should be also True.
        if self.validated_data.get("is_published"):
            self.instance.is_first_published = True
        return super().save(**kwargs)
        
    def validate_instruction(self, value):
        # check for base64encoded string or not
        try:
            if not (base64.b64encode(base64.b64decode(value)).decode() == value):
                raise ValidationError({"instruction": "Instruction must be base64 endcoded!"})
            return value
        except Exception as e:
            raise ValidationError({"instruction": e})
        
    def validate_grading_criteria(self, value):
        serializer = GradingCriteriaSerializer(data=value)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        return value
        
        
class AttachmentSerializer(BaseModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"
        
    expandable_fields = {
        "assignment": ("app_assignment.serializers.AssignmentSerializer",),
    }
        

class SubmissionSerializer(BaseModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"
        
    expandable_fields = {
        "assignment": ("app_assignment.serializers.AssignmentSerializer",),
        "submissionattachment_set": ("app_assignment.serializers.SubmissionAttachmentSerializer", {"many": True},),
    }
    
    def validate(self, attrs):
        # check for base64encoded string or not
        if not (base64.b64encode(base64.b64decode(attrs['description'])).decode() == attrs['description']):
            raise ValidationError("Description must be base64 endcoded!")
        return attrs
        

class SubmissionAttachmentSerializer(BaseModelSerializer):
    class Meta:
        model = SubmissionAttachment
        fields = "__all__"
        
    expandable_fields = {
        "submission": ("app_assignment.serializers.SubmissionSerializer",),
    }