import os


def get_env(key: str, default_value="") -> str:
    """
    Gets environment variable.

    Parameters:
        key (str): Environment variable name.
        default_value (str): Default value if environment variable is not set.

    Returns:
        str: Environment variable value.
    """
    return os.environ.get(key, default_value)
