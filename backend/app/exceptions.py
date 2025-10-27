class ServiceError(Exception):
    status_code: int=500
    error: str="ServiceError"
    message: str="Service Error"

    def __init__(self, message: str | None=None, *,status_code: int | None=None):
        if status_code is not None:
            self.status_code=status_code
        super().__init__(message or self.message)

class InvalidDateFormat(ServiceError):
    status_code=400
    error="InvalidDateFormat"
    message="Invalid date format. Use YYYY-MM-DD"

class DateOutOfRange(ServiceError):
    status_code=400
    error="DateOutOfRange"
    message="Date out of allowed range (1900..2100)"

class CarNotFound(ServiceError):
    status_code = 404
    error="CarNotFound"
    message="Car not found"

class ClaimNotFound(ServiceError):
    status_code=404
    error="ClaimNotFound"
    message="Claim not found"