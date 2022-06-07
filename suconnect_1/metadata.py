from rest_framework.metadata import BaseMetadata

class CustomMetadata(BaseMetadata):

    def determine_metadata(self, request, view):
        print(view)
        return {
            "name": view.get_view_name(),
            "description": view.get_view_description()
        }