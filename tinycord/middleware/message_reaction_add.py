import typing

from tinycord.utils.snowflake import Snowflake

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import ReactionGateway, Reaction, Emoji
    
async def message_reaction_add(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a reaction is added to a message.
        It does prase the reaction data and returns the event with the reaction.
    
        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """

    guild_id = Snowflake(event.data['guild_id'])
    """ The guild id of the reaction ."""

    event.data['emoji'] = Emoji(client, guild_id , **event.data['emoji'])

    reaction = ReactionGateway(client, **event.data)
    """ The reaction that was created. """

    user = client.get_user(reaction.user_id)
    """ The user that added the reaction. """

    message = client.get_message(reaction.message_id)
    """ The message that the reaction was added to. """
    
    if user.id == client.user.id:
        event.data['me'] = True
        """ Whether the user that added the reaction was the client. """
    else:
        event.data['me'] = False
        """ Whether the user that added the reaction was the client. """

    msg_reaction = message.get_reaction(reaction.emoji.id)
    """ The reaction that was added. """

    if msg_reaction is not None:
        event.data['count'] = msg_reaction.count + 1
        """ The count of the reaction that was added. """
    else:
        event.data['count'] = 0

    message.reactions[str(reaction.emoji.id)] = Reaction(client, **event.data)
    """ Added the reaction to the message."""
    
    return "on_message_reaction_add", [
        reaction
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return message_reaction_add