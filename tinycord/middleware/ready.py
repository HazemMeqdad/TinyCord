import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import User
    
async def ready(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    
    client.unavailable_guilds = [int(guild['id']) for guild in event.data.get('guilds')]
    client.user = User(client, **event.data.get('user'))

    return "on_ready", [
        
    ]

def export():
    return ready