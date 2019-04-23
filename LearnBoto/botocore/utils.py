import logging

logger = logging.getLogger(__name__)

def ensure_boolean(val):
    """Ensures a boolean value if a string or boolean is provided

    For strings, the value for True/False is case insensitive
    """
    if isinstance(val, bool):
        return val
    else:
        return val.lower() == 'true'