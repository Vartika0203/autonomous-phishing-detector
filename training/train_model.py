import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load processed data
X = pd.read_csv("data/processed/features.csv")
y = pd.read_csv("data/processed/labels.csv").values.ravel()

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=15,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")

# Save model and scaler
joblib.dump(model, "models/trained/url_phishing_model.pkl")
joblib.dump(scaler, "models/trained/scaler.pkl")

print("Model and scaler saved successfully.")
