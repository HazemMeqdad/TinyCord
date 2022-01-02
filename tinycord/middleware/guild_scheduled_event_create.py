import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import ScheduledEvent
    
async def scheduled_event_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when the a new scheduled event is created.
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

    scheduled_event = ScheduledEvent(client, **event.data)
    """ The scheduled event that was created. """
    
    guild = client.get_guild(scheduled_event.guild_id)
    """ The guild that the invite was created in. """

    guild.guild_scheduled_events[str(scheduled_event.id)] = scheduled_event

    return "on_scheduled_event_create", [
        guild, scheduled_event
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return scheduled_event_create