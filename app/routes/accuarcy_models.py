from fastapi import APIRouter, HTTPException, Request
from app.services.rate_limiter import rate_limit
from app.utils.models_accuracy import MODELS_ACCURACY

router = APIRouter()

@router.get("/accuracy_models", response_model=list[dict])
@rate_limit(max_calls=5, period=60)
async def accuracy_models_router(
    request: Request
):
    """
    Retorna uma lista de modelos e suas respectivas acurácias em porcentagem.
    """
    try:
        # Convertendo as acurácias para porcentagem
        models_with_percentage = [
            {"model": model["model"], "accuracy": round(model["accuracy"] * 100, 2)}
            for model in MODELS_ACCURACY
        ]
        return models_with_percentage
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
