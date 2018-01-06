
import logging
from config import LOG_FILE

logger = logging.getLogger('weibo')
logger.setLevel(logging.DEBUG)

# log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

if LOG_FILE:
    fh = logging.FileHandler('log.log')
    fh.setLevel( logging.DEBUG )
    fh.setFormatter(formatter)
    logger.addHandler(fh)
else:
    # console log
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
