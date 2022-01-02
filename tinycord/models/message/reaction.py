import typing

if typing.TYPE_CHECKING:
    from ...client import Client

from ..guild import Emoji

class Reaction:
    """
        This is the Reaction it used to represent a reaction.

        Parameters
        ----------
        bot : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the reaction.

        Attributes
        ----------
        count : `int`
            The count of the reaction.
        me : `bool`
            Whether the user is bot or not.
        emoji : `Emoji`
            The emoji.
    """
    def __init__(self, client: "Client" , **data) -> None:
        self.count: int = data.get('count')
        """The count of the reaction."""

        self.me: bool = data.get('me')
        """Whether the user is bot or not."""

        self.emoji: Emoji = Emoji(client, data.get('emoji'))
        """The emoji."""