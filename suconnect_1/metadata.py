from dataclasses import field
from rest_framework.metadata import BaseMetadata

class CustomMetadata(BaseMetadata):

    def determine_metadata(self, request, view):
        fields = [
            {
                "name": i.name,
                "type": i.get_internal_type(),
                "description": getattr(i, "help_text"),

            } for i in 
            view.model._meta.get_fields()
            ]

        return {
            "name": view.get_view_name(),
            "description": view.get_view_description(),
            "fields":fields
        }