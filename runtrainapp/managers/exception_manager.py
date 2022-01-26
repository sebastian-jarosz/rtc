from ..utils.exceptions import *


# Raise authorization exception
def raise_auth_exception(user):
    raise AuthException(user)


# Raise Http exception
# Default status code - Unknown
def raise_http_exception(status_code="Unknown"):
    raise HttpException(status_code)
