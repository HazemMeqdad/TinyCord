import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import ThreadChannel, ThreadMember

async def thread_list_sync(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a when access to a thread.
        It does prase the thread data and returns the event with the guild, before, after, members.

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

    before = [guild.get_thread(id) for id in event.data.get('channels_ids', [])]
    """ The before thread. """

    after = [ThreadChannel(client, guild_id=event.data["guild_id"], **data) for data in event.data.get('threads')]
    """ The after thread. """

    members = { data['user_id'] : ThreadMember(client, **data) for data in event.data['members']}
    """ The members that are in the thread. """

    return "on_thread_list_sync", [
        guild, before, after, members
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return thread_list_sync