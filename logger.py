import logging
import os
from datetime import datetime

# Fixed log directory inside the Elastic Beanstalk environment
log_dir = "logs"

# Ensure the logs directory exists
os.makedirs(log_dir, exist_ok=True)

# Create a log file with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
