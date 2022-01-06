import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import ThreadMember

async def on_thread_members_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when anyone is added to or removed from a thread.
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

    thread = guild.get_thread(event.data["id"])
    """ The thread that the member was added to or removed from. """

    thread.member_count = event.data["member_count"]
    """ The member count of the thread. """

    after = {data['user_id'] : ThreadMember(client, **data) for data in event.data["members"]}
    """ The members that are in the thread. """

    thread.members.update(after)

    before = [thread.get_member(id) for id in event.data.get('removed_members_ids', [])]
    """ The before members. """

    return "on_thread_members_update", [
        guild, thread, before, after
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return on_thread_members_update