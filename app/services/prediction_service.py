from app.utils.sentiment_mapping import assign_sentiment_alias
from app.config.paths import VECTORIZER_PATH
from joblib import load

vectorizer = load(VECTORIZER_PATH)

def predict_prompt(model, prompt: str) -> str:
    """
    Faz a previsão de sentimento baseada no texto e no modelo escolhido.
    
    Args:
        model: O modelo treinado para fazer a previsão.
        vectorizer: O vetorizador usado para transformar o texto.
        prompt: O texto de entrada para análise.

    Returns:
        str: O sentimento previsto (negative, neutral, positive ou unknown).
    """
    if not prompt:
        raise ValueError("The prompt cannot be empty.")
    
    if not model or not vectorizer:
        raise ValueError("Model and vectorizer must be provided.")
    
    # Transforma o texto em uma representação numérica
    vectorized_prompt = vectorizer.transform([prompt])
    
    # Faz a previsão
    prediction = model.predict(vectorized_prompt)[0]
    
    # Mapeia a previsão para um sentimento
    return assign_sentiment_alias(int(prediction))

def predict_prompt_multi_models(models: dict, prompt: str) -> dict:
    """
    Faz a previsão de sentimento baseada no texto e em todos os modelos disponíveis.
    
    Args:
        models: Um dicionário contendo todos os modelos treinados para fazer a previsão.
        vectorizer: O vetorizador usado para transformar o texto.
        prompt: O texto de entrada para análise.

    Returns:
        dict: Um dicionário contendo o sentimento previsto para cada modelo.
    """
    if not prompt:
        raise ValueError("The prompt cannot be empty.")
    
    if not models or not vectorizer:
        raise ValueError("Models and vectorizer must be provided.")
    
    # Transforma o texto em uma representação numérica
    vectorized_prompt = vectorizer.transform([prompt])
    
    # Faz a previsão para cada modelo
    predictions = {}
    for model_name, model in models.items():
        prediction = model.predict(vectorized_prompt)[0]
        predictions[model_name] = assign_sentiment_alias(int(prediction))
    
    return predictions
