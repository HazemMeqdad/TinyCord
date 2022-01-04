import typing
import asyncio

if typing.TYPE_CHECKING:
    from ..client import Client

from .channel import ChannelAPI
from .guild import GuildAPI
from .user import UserAPI

class APIClient(ChannelAPI, GuildAPI, UserAPI):
    def __init__(self, client: "Client") -> None:
        self.client = client
        """The client."""

        super(ChannelAPI, self).__init__(client)
        """The channel api."""

        super(GuildAPI, self).__init__(client)
        """The guild apis."""

        super(UserAPI, self).__init__(client)
        """The user api."""