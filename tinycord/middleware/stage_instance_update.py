import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import StageChannel
    
async def stage_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a stage channel is updated.
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
    after = StageChannel(client, **event.data['channel'])
    """ The stage channel that was updated. """

    before = client.get_channel(after.id)
    """ The stage channel that was updated. """

    guild = client.get_guild(after.guild_id)
    """ The guild that the stage channel was updated in. """

    guild.channels[str(after.id)] = after
    client.channels[str(after.id)] = after
    """ Cache the stage channel. """

    return "on_stage_update", [
        guild, before, after
    ]
    """ The event that was dispatched. """


def export():
    """ Exports the function. """
    return stage_update