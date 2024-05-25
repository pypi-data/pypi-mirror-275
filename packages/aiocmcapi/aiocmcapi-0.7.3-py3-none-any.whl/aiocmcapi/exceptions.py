class NoDataResponse(Exception):
    def __init__(self, status: dict):
        super().__init__(f"{status['error_code']}: {status['error_message']}")

class EndpointNotFound(Exception):
    def __init__(self, endpoint: str):
        super().__init__(f"'{endpoint}' endpoint not found")