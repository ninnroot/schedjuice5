from django.shortcuts import render
from rest_framework import status
from .utilities import format_fields, get_model_names
from schedjuice5.views import BaseView

# Create your views here.

def home(request):
    models_fields = format_fields()
    models_list = get_model_names()
    return render(request, 'index.html', context={'models_fields': models_fields, "models_list": models_list})


class ModelsDocsView(BaseView):
    name = "Models Docs View"
    
    def get(self, request):
        models_fields = format_fields()
        model_name = request.query_params.get("model")
        
        if model_name:
            if model_name.lower() == "lists":
                model_lists = get_model_names()
                return self.send_response(
                False,
                'Success',
                model_lists,
                status=status.HTTP_200_OK
            )
            
            else:
                for model in models_fields:
                    if model_name.capitalize() == model["model_name"]:
                        return self.send_response(
                        False,
                        'Success',
                        {"data": model},
                        status=status.HTTP_200_OK)
                return self.send_response(
                        True,
                        'Success',
                        {"Error": "Model doesn't exist."},
                        status=status.HTTP_200_OK
            )
            
        return self.send_response(
            False,
            'Success',
            {"data": models_fields},
            status=status.HTTP_200_OK
        )
