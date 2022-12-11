from django.shortcuts import render
from .utilities import format_fields

# Create your views here.

def home(request):
    models_fields = format_fields()
    return render(request, 'index.html', context={'models_fields': models_fields})
