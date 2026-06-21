from fastapi import APIRouter
from ml.predict import predict
from schemas.ml import churnpredict

router = APIRouter()

@router.post("/predict")
def ml_predict(data: churnpredict):
    features = [
        data.age,
        data.usage,
        data.support_calls
    ]
    return predict(features)