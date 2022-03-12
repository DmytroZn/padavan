import sys
from loguru import logger

logger.add(sys.stderr, format="{time:YYYY-MM-DD at HH:mm:ss} sdf {level} {message}", filter="__main__", level="INFO")
logger.add("log.log", rotation="1 day", retention="2 day")

