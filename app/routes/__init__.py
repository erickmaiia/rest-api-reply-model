from fastapi import APIRouter
from .single_model import router as single_model_router
from .multi_model import router as multi_model_router
from .accuarcy_models import router as accuarcy_models_router

router = APIRouter()

router.include_router(accuarcy_models_router, tags=["Accuracy Models"])
router.include_router(single_model_router, tags=["Single Model Prediction"])
router.include_router(multi_model_router, tags=["Multi Model Prediction"])
