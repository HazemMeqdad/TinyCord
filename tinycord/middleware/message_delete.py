import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Message
    
async def message_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    message = client.get_message(event.data['id'])

    try:
        client.messages.remove(message)
    except:
        pass
    
    return "on_message_delete", [
        message
    ]

def export():
    return message_update