import django.apps


def get_models():
    return django.apps.apps.get_models()

def get_model_names():
    models = get_models()
    model_names = [model.__name__ for model in models]
    return {"model_lists": model_names}

def format_fields():
    models = get_models()
    models_fields = []
    for m in models:
        model = {}
        model["model_name"] = m.__name__.capitalize()
        model["fields"] = []
        for f in m._meta.get_fields():
            field = {}
            field["type"] = f.get_internal_type()
            field["name"] = f.name
            model["fields"].append(field)
        models_fields.append(model)

    return models_fields
