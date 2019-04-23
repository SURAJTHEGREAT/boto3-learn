import logging

logger = logging.getLogger(__name__)

class Session(object):

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None,
                 aws_session_token=None, region_name=None,
                 botocore_session=None, profile_name=None):
        if botocore_session is not None:
            self._session = botocore_session
        else:
            # Create a new default session
            self._session = botocore.session.get_session()