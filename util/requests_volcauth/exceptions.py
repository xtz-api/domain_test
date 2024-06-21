class RequestsVolcAuthException(Exception):
    pass


class DateMismatchError(RequestsVolcAuthException):
    pass


class NoSecretKeyError(RequestsVolcAuthException):
    pass


class DateFormatError(RequestsVolcAuthException):
    pass
