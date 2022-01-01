import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Message
    
async def message_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    after = Message(client, **event.data)
    before = client.get_message(after.id)

    client.messages[str(after.id)] = after

    return "on_message_update", [
        before, after
    ]

def export():
    return message_update