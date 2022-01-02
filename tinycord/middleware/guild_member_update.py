import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Member

async def guild_member_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a member is updated.
        It does provide the guild and the member that been updated.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    after = Member(client, **event.data)
    """ The member that was updated. """

    guild = client.get_guild(after.guild_id)
    """ The guild that the member was updated in. """

    before = guild.get_member(after.id)
    """ The old member. """

    guild.members[str(after.id)] = after
    """ Caches the member. """

    return "on_member_update", [
        guild, before, after
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return guild_member_update