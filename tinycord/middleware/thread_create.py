import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import ThreadChannel
    
async def thread_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a thread is created.
        It does prase the thread data and returns the event with the thread.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """

    thread = ThreadChannel(client, **event.data)
    """ The thread that was created. """

    guild = client.get_guild(thread.guild_id)
    """ The guild that the thread was created in. """

    client.threads[str(thread.id)] = thread
    guild.channels[str(thread.id)] = thread
    """ Cache the thread. """

    return "on_thread_create", [
        guild, thread
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return thread_create