import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch


async def on_member_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a user is removed from a guild.
        It does provide the guild and the member that was removed.

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
    """ The guild that the user was removed from. """

    member = guild.get_member(event.data["user"]["id"])
    """ The member that was removed. """

    try:
        del guild.members[str(member.id)]
        """ Removes the member from the cache. """
    except KeyError:
        pass

    return "on_member_delete", [
        guild, member
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return on_member_delete