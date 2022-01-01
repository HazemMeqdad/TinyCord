import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Voicestate
    
async def voice_state_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    after = Voicestate(client, **event.data)
    guild = client.get_guild(after.guild_id) or None
    before = client.get_voicestate(after.user_id)

    try:
        client.voice_states.remove(before)
        client.voice_states.append(after)

        guild.voice_states.remove(before)
        guild.voice_states.append(after)
    except:
        pass

    return "on_vocie_state_update", [
        guild, before, after
    ]

def export():
    return voice_state_update