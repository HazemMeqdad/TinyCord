import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Voicestate
    
async def voice_state_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a voice state is updated.
        It does prase the voice state data and returns the event with the guild and the voice state.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    after = Voicestate(client, **event.data)
    """ The voice state that was updated. """

    guild = client.get_guild(after.guild_id) or None
    """ The guild that the voice state was updated in. """

    before = guild.get_integration(after.user_id)
    """ The voice state that was updated. """

    return "on_vocie_state_update", [
        guild, before, after
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return voice_state_update