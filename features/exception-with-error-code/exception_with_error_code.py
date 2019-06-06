from enum import Enum, unique

@unique
class ErrorCode(Enum):
    """ Status Code for Exceptions  """
    SUCCESS                 = 200
    EMPTY_CONTENT_EXCEPTION = 400
    ERROR                   = 500
    EXTERNAL_API_EXCEPTION  = 501
    DATABASE_EXCEPTION      = 502

class AttributeMissingException(Exception):
    code      = ErrorCode.SUCCESS
    log_level = 'warning'

class EmptyContentException(Exception):
    code      = ErrorCode.EMPTY_CONTENT_EXCEPTION
    log_level = 'warning'

class ExternalAPIException(Exception):
    code      = ErrorCode.EXTERNAL_API_EXCEPTION
    log_level = 'error'

class DatabaseException(Exception):
    code      = ErrorCode.DATABASE_EXCEPTION
    log_level = 'error'

TRACKED_EXCEPTIONS = [
    AttributeMissingException, EmptyContentException, AppConfigError,
    ExternalAPIException, DatabaseException
] # if not tracked, return ErrorCode.ERROR (500) 
