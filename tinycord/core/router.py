class Router:
    def __init__(self, path: str, method: str) -> None:
        self.path = f'https://discord.com/api/v9{path}'
        """The path of the route."""

        self.method = method
        """The method of the route."""