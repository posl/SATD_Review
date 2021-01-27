class KnowUnknownJsonError(Exception):
    pass

class QueryFileNotFoundError(FileNotFoundError):
    pass

class DetailFileNotFoundError(FileNotFoundError):
    pass

class DiffFileNotFoundError(FileNotFoundError):
    pass

class DiffLineFileNotFoundError(FileNotFoundError):
    pass

class NotTargetSubProjectException(Exception):
    pass

class NoContentsException(Exception):
    pass

class InternalServerError(Exception):
    pass

class SelfReviewFoundException(Exception):
    pass