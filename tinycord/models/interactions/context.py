import typing
from tinycord.models.guild.member import Member
from tinycord.models.message.message import Message
from tinycord.models.user.user import User

from tinycord.utils.snowflake import Snowflake
from .option import Option, SelectOption
from .types import CommandApplictionTypes
from .command import ApplictionCommand

if typing.TYPE_CHECKING:
    from ...client import Client
    from ...core import Gateway, GatewayDispatch


class SlashContext:
    """
        A command can be used in a variety of contexts, such as a chat input, a user context, a message context, etc.

        Parameters
        ---------
        id: :class:``Snowflake``
            The ID of the command.
        command: :class:``ApplictionCommand``
            The command to be used.
        type: :class:``CommandApplictionTypes``
            The type of appliction the command is used in.
        application_id: :class:``Snowflake``
            The ID of the application the command is used in.
        command_id: :class:``Snowflake``
            The ID of the command.
        name: :class:``str``
            The name of the command.
        options: :class:``list[Option]``
            The options of the command.
        component_type: :class:``Snowflake``
            the component type
        values: :class:``SelectOption``
            the values of the component
        target_id: :class:``Snowflake``
            the target id of the component
        guild_id: :class:``Snowflake``
            The ID of the guild the command is used in.
        channel_id: :class:``Snowflake``
            The ID of the channel the command is used in.
        member: :class:``Member``
            The member that is used to execute the command.
        user: :class:``User``
            The user that is used to execute the command.
        version: :class:``Snowflake``
            The version of the command.
        message: :class:``Message``
            The message that is used to execute the command.
        """
    def __init__(self, client: "Client", type: CommandApplictionTypes, **data):
        self.id: Snowflake = data.get('id')
        self.command: ApplictionCommand = data.get('command')
        self.type: "CommandApplictionTypes" = type
        self.application_id: Snowflake = data.get('application_id')
        self.command_id: Snowflake = data.get("command_id")
        self.name: str = data.get("name")

        # soon i will add the rest of the data
        # self.resolved: Snowflake = data.get("data").get("resolved") 

        self.options: list[Option] = data.get("options")
        self.custom_id: Snowflake = data.get("custom_id")
        self.component_type: Snowflake = data.get("component_type")
        self.values: SelectOption = data.get("values")
        self.target_id: Snowflake = data.get("target_id")

        self.guild_id: Snowflake = data.get("guild_id")
        self.channel_id: Snowflake = data.get("channel_id")
        self.member: Member = data.get("member")
        self.user: User = data.get("user")
        self.token: str = data.get("token")
        self.version: Snowflake = data.get("version")
        self.message: Message = data.get("message")
        
        
