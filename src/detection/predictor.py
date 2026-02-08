import joblib
import numpy as np
from src.utils.logger import get_system_logger, get_phishing_logger
from src.explainability.explanation_engine import explain_prediction

system_logger = get_system_logger()
phishing_logger = get_phishing_logger()

model = joblib.load("models/trained/url_phishing_model.pkl")
scaler = joblib.load("models/trained/scaler.pkl")

FEATURE_NAMES = [
    "url_length",
    "has_ip",
    "has_https",
    "domain_age",
    "has_at",
    "has_forms",
    "redirect_count",
    "subdomain_count"
]

def predict_phishing(features):
    features_np = np.array(features, dtype=float).reshape(1, -1)
    scaled_features = scaler.transform(features_np)

    prob = model.predict_proba(scaled_features)[0][1]
    prob = round(float(prob), 2)

    explanation = explain_prediction(features, FEATURE_NAMES)

    if prob >= 0.6:
        prediction = "Phishing"
        phishing_logger.warning(
            f"PHISHING | Risk={prob} | Reasons={explanation}"
        )
    else:
        prediction = "Legitimate"
        system_logger.info(
            f"LEGITIMATE | Risk={prob} | Reasons={explanation}"
        )

    return prediction, prob, explanation
