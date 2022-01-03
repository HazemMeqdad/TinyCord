import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch
    
async def scheduled_event_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when the a new scheduled event is deleted.
        It does does provide the scheduled event and guild.

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
    """ The guild that the scheduled event deleted in. """

    scheduled_event = guild.get_scheduled_event(event.data["id"])
    """ The scheduled event that was deleted. """

    del guild.guild_scheduled_events[str(scheduled_event.id)]

    return "on_scheduled_delete", [
        guild, scheduled_event
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return scheduled_event_delete