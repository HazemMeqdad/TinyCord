import typing

if typing.TYPE_CHECKING:
    from ..client import Client

from ..core import Router
from ..models import User

class WebhookAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client
        """The client."""