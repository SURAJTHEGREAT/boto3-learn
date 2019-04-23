import logging

__author__ = 'Suraj'
__version__ = '1.9.134'

logger = logging.getLogger(__name__)
# The default Boto3 session; autoloaded when needed.
DEFAULT_SESSION = None

def resource(*args,**kwargs):

    return _get_default_session.resource(*args,**kwargs)

def _get_default_session():

    if DEFAULT_SESSION is None:

        setup_default_session()

    # will return the session method as DEFAULT_SESSION will be maintained as GLOBAL
    return DEFAULT_SESSION

def setup_default_session(**kwargs):

    global DEFAULT_SESSION

    DEFAULT_SESSION = Session(**kwargs)



