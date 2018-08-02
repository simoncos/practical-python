from enum import Enum, unique

""" Status Code for Exceptions  """

@unique
class ErrorCode(Enum):

    SUCCESS = 200

    ERROR = 500

    DATABASE_ERROR = 501

    EMPTY_CONTENT_EXCEPTION = 400

""" Raised Exceptions  """

class DataBaseError(Exception):
    code = ErrorCode.DATABASE_ERROR
    log_level = 'error'

class EmptyContentException(Exception):
    code = ErrorCode.EMPTY_CONTENT_EXCEPTION
    log_level = 'warning'

class AttributeMissingException(Exception):
    code = ErrorCode.SUCCESS
    log_level = 'warning'

TRACKED_EXCEPTIONS = [DataBaseError, EmptyContentException, AttributeMissingException]


if __name__ == '__main__':
    print(ErrorCode.SUCCESS.value)
    print(DataBaseError('test').code==501)
    print(DataBaseError('test').log_level)
    print(type(DataBaseError('test')) in [DataBaseError, EmptyContentException, AttributeMissingException])