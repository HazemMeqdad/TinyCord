import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import ThreadMember

async def on_thread_member_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when the thread member object for the current user is updated.
        It does prase the thread data and returns the event with the guild, thread, member.

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
    """ The guild that the thread was created in. """

    thread = guild.get_thread(event.data['id'])
    """ The thread that the member was added to or removed from. """

    member = ThreadMember(client, **event.data)
    """ The member that is in the thread. """

    thread.member = member
    """ Update the thread member """

    return "on_thread_members_update", [
        guild, thread, thread.member
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return on_thread_member_update