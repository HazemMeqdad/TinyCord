import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Message
    
async def message_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a message is deleted.
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
    message = client.get_message(event.data['id'])
    """ The message that was deleted. """

    try:
        del client.messages[str(message.id)]
        """ Try to delete the message from the cache. """
    except KeyError:
        pass
    
    return "on_message_delete", [
        message
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return message_delete