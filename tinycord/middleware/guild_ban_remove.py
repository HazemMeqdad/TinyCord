import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import User

async def guild_ban_remove(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a user is unbanned from a guild.
        It does provide the guild and the user that was unbanned.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    user = User(client, **event.data['user'])
    """ The user that was unbanned. """

    guild = client.get_guild(event.data['guild_id'])
    """ The guild that the user was unbanned from. """

    return "on_ban_remove", [
        guild, user
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return guild_ban_remove