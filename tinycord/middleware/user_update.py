import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import User
    
async def user_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a user is updated.
        It does prase the user data and returns the event with the user.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    after = User(client, **event.data['user'])
    """ The user that was updated. """

    before = client.get_user(after.id)
    """ The user that was updated. """

    client.users[str(after.id)] = after
    """ Cache the user. """

    return "on_user_update", [
        before, after
    ]
    """ The event that was dispatched. """

def export():
    return user_update