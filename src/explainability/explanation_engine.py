def explain_prediction(features, feature_names, threshold=0.6):
    """
    Generates human-readable explanation for phishing detection.
    """

    explanation = []

    feature_map = dict(zip(feature_names, features))

    if feature_map["domain_age"] < 30:
        explanation.append("Domain age is very low")

    if feature_map["has_https"] == 0:
        explanation.append("HTTPS is not used")

    if feature_map["has_forms"] == 1:
        explanation.append("Credential collection form detected")

    if feature_map["subdomain_count"] > 3:
        explanation.append("Excessive subdomains detected")

    if feature_map["redirect_count"] > 1:
        explanation.append("Multiple redirects detected")

    if feature_map["has_ip"] == 1:
        explanation.append("IP-based URL detected")

    if not explanation:
        explanation.append("No strong phishing indicators found")

    return explanation