import logging
import logging.config
import yaml
import os

def setup_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    with open("config/logging.yaml", "r") as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)

def get_system_logger():
    return logging.getLogger("system")

def get_phishing_logger():
    return logging.getLogger("phishing")
