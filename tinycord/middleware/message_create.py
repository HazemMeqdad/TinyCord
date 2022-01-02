import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Message
    
async def message_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a message is created.
        It does prase the message data and returns the event with the channel and the message.
    
        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    message = Message(client, **event.data)
    """ The message that was created. """

    client.messages[str(message.id)] = message
    """ Cache the message. """
    
    return "on_message", [
        message
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return message_create