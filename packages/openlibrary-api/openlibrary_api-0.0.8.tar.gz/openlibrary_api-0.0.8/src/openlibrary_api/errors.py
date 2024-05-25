class OLAPIException(Exception):
    "Base class for Exceptions in the openlibrary_api package"
    def __init__(self, message: str):
        super().__init__(self, "OpenLibrary API Exception: " + message)

class StatusCodeException(OLAPIException):
    "Exception for response status codes"
    def __init__(self, response_code: int, request: str):
        match(response_code):
            case 400:
                super().__init__(f"Bad Request: {request}")
            case 403:
                super().__init__(f"This page cannot be accessed: {request}")
            case 404: 
                super().__init__(f"Page not found: {request}")
            case 429:
                super().__init__(f"Rate Limited: {request}")
            case 500:
                super().__init__(f"Internal Server Error: {request}")
            case 503:
                super().__init__(f"Server is down: {request}")
            case _:
                super().__init__(f"Unexpected response code {response_code}: {request}")

class APIErrorException(OLAPIException):
    "Exception for if an error is returned by the request"
    def __init__(self, response_error: str, request):
        match(response_error):
            case "not found":
                super().__init__(f"Item Not Found: {request}")