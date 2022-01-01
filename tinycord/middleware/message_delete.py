import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Message
    
async def message_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    message = client.get_message(event.data['id'])

    try:
        del client.messages[str(message.id)]
    except KeyError:
        pass
    
    return "on_message_delete", [
        message
    ]

def export():
    return message_delete