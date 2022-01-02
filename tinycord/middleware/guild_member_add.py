import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Member

async def guild_member_add(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a user is added to a guild.
        It does provide the guild and the member that was added and caches the member.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    member = Member(client, **event.data)
    """ The member that was added. """

    guild = client.get_guild(member.guild_id)
    """ The guild that the member was added to. """

    guild.members[str(member.id)] = member
    """ Caches the member. """

    return "on_member_create", [
        guild, member
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return guild_member_add