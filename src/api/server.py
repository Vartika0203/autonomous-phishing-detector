from fastapi import FastAPI
from pydantic import BaseModel, Field
from src.detection.predictor import predict_phishing

app = FastAPI(
    title="Autonomous Phishing Detector API",
    description="Explainable phishing detection backend",
    version="1.0.0"
)

# -----------------------------
# Request schema
# -----------------------------
class PhishingRequest(BaseModel):
    url_length: int = Field(..., example=42)
    has_ip: int = Field(..., example=0)
    has_https: int = Field(..., example=1)
    domain_age: int = Field(..., example=120)
    has_at: int = Field(..., example=0)
    has_forms: int = Field(..., example=1)
    redirect_count: int = Field(..., example=2)
    subdomain_count: int = Field(..., example=3)

# -----------------------------
# Response schema
# -----------------------------
class PhishingResponse(BaseModel):
    prediction: str
    risk_score: float
    reasons: list[str]

# -----------------------------
# Health check
# -----------------------------
@app.get("/")
def health():
    return {"status": "API is running"}

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict", response_model=PhishingResponse)
def predict(data: PhishingRequest):
    features = [
        data.url_length,
        data.has_ip,
        data.has_https,
        data.domain_age,
        data.has_at,
        data.has_forms,
        data.redirect_count,
        data.subdomain_count
    ]

    prediction, score, reasons = predict_phishing(features)

    return {
        "prediction": prediction,
        "risk_score": score,
        "reasons": reasons
    }