# Threat Model – Autonomous Phishing Detector

## Threat Overview
Phishing attacks exploit deceptive URLs, credential harvesting forms, and redirection chains.

## Attack Vectors Addressed
- Short-lived malicious domains
- URLs without HTTPS
- Credential collection pages
- Excessive redirects
- IP-based URLs

## Detection Strategy
The system uses supervised machine learning combined with heuristic features to assess phishing risk.

## Security Controls
- Input validation via FastAPI & Pydantic
- Explainable detection outputs
- Logging of phishing events
- Strict feature-order enforcement

## Limitations
- Does not perform live URL crawling
- Depends on pre-extracted features