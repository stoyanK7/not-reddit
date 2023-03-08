""""This module is used to get environment variables from .env file"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_env(key) -> str:
    """
    Gets environment variable.

    Parameters:
        key (str): Environment variable name.

    Returns:
        str: Environment variable value.
    """
    return os.getenv(key)
