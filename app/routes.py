#!/usr/bin/env python3
"""
"""

from flask import Blueprint, request, render_template
from .predictor import load_model, predict

main = Blueprint("main", __name__)

model = load_model()


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.get_json()
    prediction = predict(model, data)
    return {
        "status": "success",
        "data": {
            "prediction": prediction["prediction"],
            "probability": prediction["probability"]
        }
    }, 200
