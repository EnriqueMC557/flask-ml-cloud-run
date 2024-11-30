#!/usr/bin/env python3
"""
"""
import joblib

import numpy as np

from .preprocess import preprocess


def load_model():
    model = joblib.load("app/predictor/files/model.pkl")
    return model


def predict(model, data):
    data = preprocess(data)
    prediction_proba = model.predict_proba(data)

    return {
        "prediction": int(np.argmax(prediction_proba)),
        "probability": [round(float(prob*100), 2) for prob in prediction_proba[0]]
    }
