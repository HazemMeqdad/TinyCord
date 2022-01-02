import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

async def stage_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a stage channel is created.
        It does prase the stage channel data and returns the event with the channel and the stage channel.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    guild = client.get_guild(event.data['guild_id'])
    """ The guild that the stage channel was created in. """

    stage = client.get_channel(event.data['id'])
    """ The stage channel that was created. """

    del client.channels[str(stage.id)]
    del guild.channels[str(stage.id)]
    """ Cache the stage channel. """
    
    return "on_stage_delete", [
        guild, stage
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return stage_create