import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import ThreadChannel
    
async def thread_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a thread is updated.
        It does prase the thread data and returns the event with the guild, before, after.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """

    after = ThreadChannel(client, **event.data)
    """ The thread that was created. """

    before = client.get_thread(after.id)
    """ The old thread. """

    guild = client.get_guild(after.guild_id)
    """ The guild that the thread was created in. """

    client.threads[str(after.id)] = after
    guild.channels[str(after.id)] = after
    """ Cache the thread. """

    return "on_thread_update", [
        guild, before, after
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return thread_update