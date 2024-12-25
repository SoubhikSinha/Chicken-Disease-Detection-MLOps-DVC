import os
import sys
import logging

# Custom Logging
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs" # Creation of 'log' directory
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) # Print the log into the terminal / CLI
    ]
)

logger = logging.getLogger("cnnClassifierLogger")