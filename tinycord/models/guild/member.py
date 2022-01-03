import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client
    from ..guild import Guild
    from ..user import Voicestate

from ..mixins import Hashable
from ...utils import Snowflake
from ..user import User

@dataclasses.dataclass(repr=False)
class Member(User, Hashable):
    """
        The member is a part from a guild.
        It's basically a member from a guild.
        It contains all the information about the member.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the member.

        Attributes
        ----------
        roles_ids : `typing.List[Snowflake]`
            The roles of the member.
        nick : `typing.Union[str, None]`
            The nickname of the member.
        avatar : `typing.Union[str, None]`
            The avatar of the member.
        joined_at : `str`
            The date the member joined the guild.
        deaf : `bool`
            Whether the member is deafened or not.
        mute : `bool`
            Whether the member is muted or not.
    """
    def __init__(self, client: "Client", guild_id: Snowflake , **data) -> None:

        self.client = client
        """The main client."""

        self.guild_id: Snowflake = guild_id
        """The ID of the guild."""

        self.roles_ids: typing.List[Snowflake] = [
            Snowflake(role) for role in data.get('roles')]
        """The roles of the member."""

        self.nick: typing.Union[str, None] = data.get('nick')
        """The nickname of the member."""

        self.avatar: typing.Union[str, None] = data.get('avatar')
        """The avatar of the member."""

        self.joined_at: str = data.get('joined_at')
        """The date the member joined the guild."""

        self.deaf: bool = data.get('deaf')
        """Whether the member is deafened or not."""

        self.mute: bool = data.get('mute')
        """Whether the member is muted or not."""

        super().__init__(client, **data.get('user'))

    @property
    def guild(self) -> typing.Union["Guild", None]:
        """The guild of the member."""

        return self.client.get_guild(self.guild_id)

    @property
    def voice_state(self) -> typing.Union["Voicestate", None]:
        """The voice state of the member."""

        return self.guild.get_voice_state(self.id)
        