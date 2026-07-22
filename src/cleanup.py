import os
from src.logger import logger

def cleanup_files(paths):

    for path in paths:

        if os.path.exists(path):
            os.remove(path)
            logger.info(f"Deleted {path}")