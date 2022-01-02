import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

async def guild_role_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a role is deleted.
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
    guild = client.get_guild(event.data["guild_id"])
    """ The guild that the role was deleted from. """

    role = guild.get_role(event.data["role_id"])
    """ The role that was deleted. """

    try:
        del guild.roles[str(role.id)]
        """ Try to delete the role from the cache. """
    except KeyError:
        pass

    return "on_role_delete", [
        guild, role 
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return guild_role_delete