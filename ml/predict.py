import joblib
import numpy as np
model = joblib.load("./ml/artifacts/model.pkl")

def predict(features):
    data = np.array(features).reshape(1,-1)

    pred = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]


    return {
        "prediction": int(pred),
        "probability": float(prob)
    }