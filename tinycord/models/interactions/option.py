from dataclasses import dataclass
import typing

from tinycord.models.guild.emoji import Emoji

from .types import Choice, ChannelType
from ...utils import Snowflake


@dataclass(init=True)
class Option:
    """
    A command option.

    Parameters
    ----------
    type: :class:`Snowflake`
        The type of option.
    name: :class:`str`
        The name of the option.
    description: :class:`str`
        The description of the option.
    required: :class:`bool`
        Whether the option is required.
    choices: :class:`list[Choice]`
        The choices of the option.
    options: :class:`list[Option]`  
        The options of the option.
    channel_types: :class:`ChannelType`
        The channel types the option is used in.
    min_value: :class:`Snowflake`
        The minimum value of the option.
    max_value: :class:`Snowflake`
        The maximum value of the option.
    autocomplete: :class:`bool`
        Whether the option is autocomplete.
    """
    def __init__(self, **data) -> None:
        self.type: Snowflake = data.get('type')
        self.name: str = data.get('name')
        self.description: str = data.get('description')
        self.required: typing.Union[bool, None] = data.get('required')
        self.choices: typing.List[Choice] = data.get('choices')
        self.options: typing.List[Option] = data.get('options')
        self.channel_types: "ChannelType" = data.get('channel_types')
        self.min_value: Snowflake = data.get('min_value')
        self.max_value: Snowflake = data.get('max_value')
        self.autocomplete: bool = data.get('autocomplete')


@dataclass
class SelectOption:
   label: str
   value: str
   description: str = None
   emoji: Emoji = None
   default: bool = False

