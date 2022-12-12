from django.shortcuts import render
from rest_framework import status
from .utilities import format_fields, get_model_names
from schedjuice5.views import BaseView

# Create your views here.

def home(request):
    models_fields = format_fields()
    return render(request, 'index.html', context={'models_fields': models_fields})


class ModelsDocsView(BaseView):
    name = "Models Docs View"
    
    def get(self, request):
        self.description = "Try adding _set or _id after ForeingnKey name xD."
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
                return self.send_response(
                False,
                'Success',
                {
                    "model_name": model_name.capitalize(),
                    "fields": models_fields[model_name.capitalize()]},
                status=status.HTTP_200_OK
            )
        
        all_model = []
        for m in models_fields:
            model = {}
            model["model_name"] = m.capitalize()
            model["fields"] = models_fields[m.capitalize()]
            all_model.append(model)
            
        return self.send_response(
            False,
            'Success',
            {"data": all_model},
            status=status.HTTP_200_OK
        )
