import json
from datetime import datetime

metadata = {
    "project": "Autonomous AI Phishing Detector",
    "model_type": "RandomForestClassifier",
    "features": [
        "url_length",
        "has_ip",
        "has_https",
        "domain_age",
        "has_at",
        "has_forms",
        "redirect_count",
        "subdomain_count"
    ],
    "training_date": datetime.now().strftime("%Y-%m-%d"),
    "dataset": "data/processed",
    "version": "1.0"
}

with open("models/trained/model_metadata.json", "w") as f:
    json.dump(metadata, f, indent=4)

print("Model metadata saved.")
