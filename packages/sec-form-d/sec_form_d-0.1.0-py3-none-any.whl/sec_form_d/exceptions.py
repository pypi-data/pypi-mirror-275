class BaseError(Exception):
    """Base error class."""
    def __init__(self, message: str):
        self.message = message

    def __repr__(self) -> str:
        return self.message

    def __str__(self) -> str:
        return repr(self)
    

class HTMLConversionError(BaseError):
    """General HTML conversion error."""
    def __init__(self, message: str):
        super().__init__(message=message)


class InvalidSectionError(BaseError):
    """General model validation error for a section."""
    def __init__(self, message: str):
        super().__init__(message=message)


class InvalidFormError(BaseError):
    """Error if the form passed is not a Form D."""
    def __init__(self, message: str):
        super().__init__(message=message)