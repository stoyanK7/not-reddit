"""This module is used to configure the logging for the application."""

import logging
from uvicorn.logging import DefaultFormatter

# Create logger.
logger = logging.getLogger('api_logger')
logger.setLevel(logging.DEBUG)

# Create console handler and set level to debug.
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatter.
FORMAT: str = "%(levelprefix)s %(message)s"
formatter = DefaultFormatter(FORMAT, datefmt="%Y-%m-%d %H:%M:%S")

# Add formatter to console handler.
console_handler.setFormatter(formatter)

# Add console handler to logger.
logger.addHandler(console_handler)
