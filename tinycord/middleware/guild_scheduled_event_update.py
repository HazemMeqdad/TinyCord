import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import ScheduledEvent
    
async def scheduled_event_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when the a new scheduled event is updated.
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

    after = ScheduledEvent(client, **event.data)
    """ The scheduled event that was updated. """

    guild = client.get_guild(after.guild_id)
    """ The guild that the scheduled event updated in. """

    before = guild.get_scheduled_event(after.id)
    """ The old scheduled event. """

    guild.guild_scheduled_events[str(after.id)] = after
    """ The new scheduled event. """

    return "on_scheduled_event_update", [
        guild, before, after
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return scheduled_event_update