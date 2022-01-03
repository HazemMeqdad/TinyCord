class GatewayError(Exception):
    """
        Base class for all gateway errors.
    """
    def __init__(self, message: str) -> None:
        self.message: str = message
        """The message of the error."""

        super().__init__(message)