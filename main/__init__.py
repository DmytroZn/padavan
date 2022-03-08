import sys
from loguru import logger

logger.add(sys.stderr, format="{time:YYYY-MM-DD at HH:mm:ss} {level} {message}", filter="my_module", level="INFO")
