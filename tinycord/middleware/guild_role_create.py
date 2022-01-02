import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Role

async def guild_role_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a role is created.
        It does prase the role data and returns the event with the guild and the role.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    role = Role(client, **event.data)
    """ The role that was created. """

    guild = client.get_guild(role.guild_id)
    """ The guild that the role was created in. """

    guild.roles[str(role.id)] = role
    """ Cache the role. """

    return "on_role_create", [
        guild, role 
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return guild_role_create