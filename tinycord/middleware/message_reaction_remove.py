import typing

from tinycord.utils.snowflake import Snowflake

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import ReactionGateway, Reaction, Emoji
    
async def message_reaction_remove(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a reaction is removed from the message.
        It does prase the reaction data and returns the event with a reaction.
    
        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    reaction = ReactionGateway(client, **event.data)
    """ The reaction that was removed. """

    message = client.get_message(reaction.message_id)
    """ The message that the reaction was added to. """

    try:
        del message.reactions[str(reaction.emoji.id)]
    except KeyError:
        pass
    """ Removed the reaction from the message. """

    return "on_message_reaction_remove", [
        reaction
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return message_reaction_remove