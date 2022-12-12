import django.apps


def get_models():
    return django.apps.apps.get_models()

def get_model_names():
    models = get_models()
    model_names = [model.__name__ for model in models]
    return {"model_lists": model_names}

def format_fields():
    models = get_models()
    models_fields = {}
    for model in models:
        models_fields[model.__name__.capitalize()] = []
        for f in model._meta.get_fields():
            field = {}
            field["type"] = f.get_internal_type()
            field["name"] = f.name
            models_fields[model.__name__.capitalize()].append(field)
    return models_fields
