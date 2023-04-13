import os

def get_env(key: str) -> str:
    """
    Gets environment variable.

    Parameters:
        key (str): Environment variable name.

    Returns:
        str: Environment variable value.
    """
    return os.environ.get(key)
