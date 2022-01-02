import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Message
    
async def message_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a message is updated.
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
    after = Message(client, **event.data)
    """ The message that was updated. """

    before = client.get_message(after.id)
    """ The message that was updated. """

    client.messages[str(after.id)] = after
    """ Cache the message. """

    return "on_message_update", [
        before, after
    ]
    """ The event that was dispatched. """

def export():
    return message_update