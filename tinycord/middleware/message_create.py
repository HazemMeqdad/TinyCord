import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Message
    
async def message_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    message = Message(client, **event.data)

    client.messages.append(message)
    
    return "on_message", [
        message
    ]

def export():
    return message_create