import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import User
    
async def ready(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when the client is ready.
        It does provide the client and the user that was ready.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    client.unavailable_guilds = [int(guild['id']) for guild in event.data.get('guilds')]
    """ The guilds that the client is unavailable from. """

    client.user = User(client, **event.data.get('user'))
    """ The user that was ready. """

    return "on_ready", [
        
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return ready