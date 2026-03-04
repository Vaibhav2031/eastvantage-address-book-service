# log_rotation.py
import logging
from logging.handlers import TimedRotatingFileHandler
import os

# Ensure the logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configure TimedRotatingFileHandler
log_file = os.path.join(LOG_DIR, "app.log")
handler = TimedRotatingFileHandler(
    log_file, when="midnight", interval=1, backupCount=7
)
handler.suffix = "%Y-%m-%d.zip"  # Automatically compress logs daily
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Add the handler to the root logger
logging.getLogger().addHandler(handler)