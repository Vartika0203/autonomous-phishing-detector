import inspect
from src.utils.logger import setup_logging, get_system_logger
from src.detection import predictor

setup_logging()
logger = get_system_logger()

logger.info("Autonomous Phishing Detector started")

# 🔍 PRINT WHERE predict_phishing IS COMING FROM
print("PREDICTOR FILE:", predictor.__file__)
print("PREDICT_PHISHING SOURCE:")
print(inspect.getsource(predictor.predict_phishing))

features = [42, 0, 0, 5, 0, 1, 2, 3]

result = predictor.predict_phishing(features)
print("RAW RETURN:", result)
print("RETURN LENGTH:", len(result))
