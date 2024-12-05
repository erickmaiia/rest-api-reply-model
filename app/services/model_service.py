from app.config.paths import MODEL_PATHS
from joblib import load


def load_model(model: str):
    if model not in MODEL_PATHS:
        raise ValueError(f"Model {model} not found.")
    
    model_path = MODEL_PATHS[model]
    model = load(model_path)
    return model

def load_models():
    models = {}
    for model in MODEL_PATHS:
        models[model] = load_model(model)
    return models
