import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch
    
async def scheduled_event_user_remove(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when the a user is added to a scheduled event.
        It does does provide the scheduled event ,guild and the user.

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
    """ The guild that the user was removed from the scheduled event in. """

    scheduled_event = guild.get_scheduled_event(event.data["id"])
    """ The scheduled event. """

    user = client.get_user(event.data["user_id"])
    """ The user that was removed to the scheduled event. """

    scheduled_event.user_count -= 1

    return "on_scheduled_event_user_remove", [
        guild, user, scheduled_event
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return scheduled_event_user_remove