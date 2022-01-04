import typing
import asyncio

if typing.TYPE_CHECKING:
    from ..client import Client

class UserAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client
        """The client."""