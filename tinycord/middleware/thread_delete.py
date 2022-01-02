import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

async def thread_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
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

    guild = client.get_guild(event.data["guild_id"])
    """ The guild that the thread was created in. """

    thread = guild.get_channel(event.data["id"])
    """ The thread that was created. """

    del client.threads[str(thread.id)]
    del guild.channels[str(thread.id)]
    """ Cache the thread. """

    return "on_thread_update", [
        guild, thread
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return thread_delete