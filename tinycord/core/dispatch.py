import typing
from json import loads


class GatewayDispatch:
    """
        Parase the gateway message

        Example:
            payload = GatewayDispatch.form(data)

        Parameters
        ----------
        op: `int`
            The opcode of the message.
        data: `typing.Dict`
            The data that comes from the websocket.
        seq: `int`
            The sequence of the message.
        event: `str`
            The event that is being called.
    """
    def __init__(
        self,
        op: int,
        data: typing.Dict,
        seq: int,
        event: str,
    ) -> None:
        self.op = op
        self.data = data
        self.seq = seq
        self.event = event

    @classmethod
    def form(cls, payload: str) -> typing.Dict[str,typing.Any]:
        """
            Parase the data and make it json
        """
        json: typing.Dict[str,typing.Any] = loads(payload)
        
        return cls(
            int(json["op"]),
            json["d"],
            json["s"],
            json["t"],
        )

    def __repr__(self) -> str:
        return f"<GatewayDispatch op={self.op} event={self.event}>"