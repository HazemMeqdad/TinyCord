import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import StageChannel
    
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
    stage = StageChannel(client, **event.data['channel'])
    """ The stage channel that was created. """

    guild = client.get_guild(stage.guild_id)
    """ The guild that the stage channel was created in. """

    guild.channels[str(stage.id)] = stage
    client.channels[str(stage.id)] = stage
    """ Cache the stage channel. """

    return "on_stage_create", [
        guild, stage
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return stage_create