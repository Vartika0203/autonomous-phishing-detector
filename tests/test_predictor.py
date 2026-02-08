from src.detection.predictor import predict_phishing

def test_predict_phishing():
    features = [42, 0, 0, 5, 0, 1, 2, 3]
    prediction, score, reasons = predict_phishing(features)

    assert prediction in ["Phishing", "Legitimate"]
    assert 0 <= score <= 1
    assert isinstance(reasons, list)