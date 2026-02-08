import streamlit as st
from src.detection.predictor import predict_phishing

st.set_page_config(
    page_title="Autonomous Phishing Detector",
    layout="centered"
)

st.title("🛡 Autonomous Phishing Detector")
st.write("Explainable ML-based phishing detection system")

st.subheader("Enter URL Features")

url_length = st.number_input("URL Length", min_value=0, value=42)
has_ip = st.selectbox("Contains IP Address?", [0, 1])
has_https = st.selectbox("Uses HTTPS?", [0, 1])
domain_age = st.number_input("Domain Age (days)", min_value=0, value=120)
has_at = st.selectbox("Contains '@' symbol?", [0, 1])
has_forms = st.selectbox("Contains Forms?", [0, 1])
redirect_count = st.number_input("Redirect Count", min_value=0, value=2)
subdomain_count = st.number_input("Subdomain Count", min_value=0, value=3)

features = [
    url_length,
    has_ip,
    has_https,
    domain_age,
    has_at,
    has_forms,
    redirect_count,
    subdomain_count
]

if st.button("🔍 Predict"):
    prediction, score, reasons = predict_phishing(features)

    st.markdown(f"### 🔎 Result: **{prediction}**")
    st.markdown(f"### ⚠ Risk Score: **{score}**")

    st.subheader("📌 Reasons")
    for r in reasons:
        st.write(f"- {r}")
