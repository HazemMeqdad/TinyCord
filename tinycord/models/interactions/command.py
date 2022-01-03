import typing
from dataclasses import dataclass

from ...utils import Snowflake
from .types import CommandApplictionTypes
from .option import Option

@dataclass(repr=True)
class ApplictionCommand:
    """
    A command can be used in a variety of contexts, such as a chat input, a user context, a message context, etc.
    
    Parameters
    ---------
    id: :class:``Snowflake``
        The ID of the command.
    type: :class:``CommandApplictionTypes``
        The type of appliction the command is used in.
    guild_id: :class:``Snowflake``
        The ID of the guild the command is used in.
    name: :class:``str``
        The name of the command.
    description: :class:``str``
        The description of the command.
    options: :class:``list[Option]``
        The options of the command.
    default_permission: :class:``bool``
        Whether the command is enabled by default.
    version: :class:``Snowflake``
        The version of the command.
    """
    def __init__(self, **data) -> None:
        self.id: Snowflake = data.get('id')
        self.type: "CommandApplictionTypes" = data.get('type')
        self.guild_id: typing.Union[Snowflake, None] = data.get('guild_id')
        self.name: str = data.get('name')
        self.description: str = data.get('description')
        self.options: typing.List[Option] = data.get('options')
        self.default_permission: bool = data.get('default_permission', True)
        self.version: Snowflake = data.get('version')





