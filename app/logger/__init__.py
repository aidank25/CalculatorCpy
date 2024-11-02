import logging
import logging.config
import os

def setup_logger():
    os.makedirs('logs', exist_ok=True)
    logging_conf_path = 'logging.conf'
    if os.path.exists(logging_conf_path):
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.propagate=True
    logging.info("Logging configured.")
