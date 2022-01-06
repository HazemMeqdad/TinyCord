import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ....client import Client
    from .member import ThreadMember

from ..channel import BaseChannel
from ...mixins import Hashable
from ....utils import Snowflake

@dataclasses.dataclass(repr=False)
class ThreadChannel(BaseChannel,Hashable):
    """
        This is the Thread it used to represent a text channel.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the channel.
    """
    def __init__(self, client: "Client", guild_id: Snowflake , **data) -> None:
        self.last_message_id: int = Snowflake(
            data.get('last_message_id'))
        """The ID of the last message."""
        
        self.message_count: int = data.get('message_count')
        """The message count."""

        self.member_count: int = data.get('member_count')
        """The member count."""

        self.members: typing.Dict[str, "ThreadMember"] = data.get('members', {})
        """The members."""

        self.member: typing.Union[None, "ThreadMember"] = data.get('member', None)
        """The member."""

        self.thread_metadata: typing.Dict[str, str] = data.get('thread_metadata')
        """The thread metadata."""

        super().__init__(client, guild_id, **data)
        """The base channel."""

    def get_member(self, id: int) -> "ThreadMember":
        """
            This is used to get a member.

            Parameters
            ----------
            id : `int`
                The user id.
        """
        return self.members.get(str(id))

    async def join(self):
        """
            This is used to join the thread.
        """
        await self.client.api.thread_join(self.id)

    async def leave(self):
        """
            This is used to leave the thread.
        """
        await self.client.api.thread_leave(self.id)
        