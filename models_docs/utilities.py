import django.apps

"""
models_fields = [
    {
        model_name_1: [
            {
                type: "CharField",
                name: "address"
            },
        ],
        model_name_2: [],
    }
]
"""

def get_models():
    return django.apps.apps.get_models()

def format_fields():
    models = get_models()
    models_fields = {}
    for model in models:
        models_fields[model.__name__] = []
        for f in model._meta.get_fields():
            field = {}
            field["type"] = f.get_internal_type()
            field["name"] = f.name
            models_fields[model.__name__].append(field)
    return models_fields
