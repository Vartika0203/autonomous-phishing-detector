# Autonomous AI Phishing Detector

## 📌 Project Overview
The Autonomous AI Phishing Detector is a cybersecurity application designed to automatically detect and classify phishing attempts using machine learning techniques. The system analyzes URLs, email content, and related metadata to determine whether an entity is phishing or legitimate and takes action without requiring continuous user input.

The project focuses on practicality, explainability, and real-world usability, making it suitable for everyday users as well as academic evaluation.

---

## 🎯 Objectives
- Detect phishing websites and emails using machine learning
- Automate phishing risk assessment and decision-making
- Reduce false positives through feature-based analysis
- Maintain detailed logs for monitoring and forensic analysis
- Provide a modular and scalable architecture

---

## 🧠 Key Features
- URL-based phishing detection
- Risk-score–based classification
- Autonomous decision logic (allow / warn / block)
- Centralized logging of system activity and phishing events
- Reproducible model training pipeline

---

## 🏗️ System Architecture
The system is divided into the following layers:

1. **Data Layer**
   - Raw phishing and legitimate datasets
   - Processed feature datasets

2. **Model Layer**
   - Machine learning model for phishing detection
   - Feature scaler and evaluation artifacts

3. **Detection Layer**
   - Loads trained models
   - Performs phishing prediction

4. **Autonomous Logic**
   - Applies thresholds to determine actions

5. **Logging Layer**
   - System logs
   - Phishing incident logs

---

## 🧪 Technologies Used
- **Programming Language:** Python 3.x
- **Machine Learning:** Scikit-learn
- **Backend Framework:** FastAPI / Flask (optional)
- **Data Handling:** Pandas, NumPy
- **Model Serialization:** Joblib
- **Logging:** Python logging module
- **Database (optional):** SQLite

---

## 📂 Project Structure
