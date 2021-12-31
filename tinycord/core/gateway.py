from __future__ import annotations

import itertools
import typing
import aiohttp
import asyncio
import logging
import zlib

from .dispatch import GatewayDispatch
from ..exceptions import GatewayError

logger: logging.Logger = logging.getLogger("tinycord")
ZLIB_SUFFIX = b'\x00\x00\xff\xff'
inflator = zlib.decompressobj()

class Gateway:
    """
        The gateway is the handler for all the events and opcodes coming from the `Discord Gateway`
    """
    def __init__(
        self,
        token: str,
        *,
        intents: typing.List[str],
        url: str,
        shard_id: int,
        shard_count: int,

        version: int = 9,
        max_retries: int = 5,
        reconnect: bool = True,
    ) -> None:
        self.token = token
        self.intents = intents
        self.url = url
        self.shard_id = shard_id
        self.shard_count = shard_count

        self.version = version
        self.max_retries = max_retries
        self.reconnect = reconnect

        self.__handler: typing.Dict[str, typing.Callable] = {
            7: self.handle_reconnect,
            9: self.handle_invalid_session,
            10: self.handle_hello,
            11: self.handle_heartbeat_ack,
        }
        self.__errors: typing.Dict[int, typing.Callable] = {
            4000: GatewayError("Unknown Error"),
            4001: GatewayError("Unknown Opcode"),
            4002: GatewayError("Decode Error"),
            4003: GatewayError("Not Authenticated"),
            4004: GatewayError("Authentication Failed"),
            4005: GatewayError("Already Authenticated"),
            4007: GatewayError("Invalid Sequence"),
            4008: GatewayError("Rate Limited"),
            4009: GatewayError("Session Timeout"),
            4010: GatewayError("Invalid Shard"),
            4011: GatewayError("Sharding Required"),
            4012: GatewayError("Invalid API Version"),
            4013: GatewayError("Invalid Intents"),
            4014: GatewayError("Disallowed Intents"),
        }

        self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        self.buffer: bytearray = bytearray()
        self.should_reconnect: bool = False
        self.sequence: int = 0
        self.session_id: int = None

        self.heartbeat_task: typing.Optional[asyncio.Task] = None
        self.heartbeat_interval: int = None
        self.heartbeat_ack: bool = False

    def append_handler(self, handlers: typing.Dict[int, typing.Callable]) -> None:
        """
            This function is used to append a handler to the gateway.

            Parameters
            ----------
            handlers: `typing.Dict[int, typing.Callable]`
                A dictionary of opcodes and their handlers.
        """
        self.__handler = {**self.__handler, **handlers}

    def append_error(self, errors: typing.Dict[int, typing.Callable]) -> None:
        """
            This function is used to append a error handler to the gateway.

            Parameters
            ----------
            errors: `typing.Dict[int, typing.Callable]`
                A dictionary of opcodes and their handlers.
        """
        self.__errors = {**self.__errors, **errors}

    def decompress(self, data: bytes) -> bytes:
        """
            This function is used to decompress the data.

            Parameters
            ----------
            data: `bytes`
                The data to decompress.
        """

        self.buffer.extend(data)
        
        if len(self.buffer) < 4 or data[-4:] != ZLIB_SUFFIX:
            return None
        
        msg = inflator.decompress(self.buffer)
        self.buffer.clear()

        return msg

    def make_url(self) -> str:
        """
            This function is used to make the url for the gateway.
        """
        return f"{self.url}?v={self.version}&encoding=json&compress=zlib-stream"

    async def send(self, op: int, payload: typing.Dict[str,typing.Any]):
        """
            |coro|
            This function is the handler for the hello opcode.
        """
        
        await self.websocket.send_json({
            "op": op,
            "d": payload,
        })

    async def send_identify(self, payload: GatewayDispatch) -> None:
        """
            |coro|
            This function is used to send the identify opcode.
        """
        if self.should_reconnect:
            logger.debug(
                f" {self.shard_id} Reconnecting to gateway..."
            )

            await self.send(
                op=6,
                payload={
                    "token": self.token,
                    "session_id": self.session_id,
                    "seq": self.sequence,
                }
            )

            return None

        await self.send(
            op=2,
            payload={
                "token": self.token,
                "properties": {
                    "$os": "linux",
                    "$browser": "tinycord",
                    "$device": "tinycord",
                },
                "compress": True,
                "large_threshold": 250,
                "shard": [self.shard_id, self.shard_count],
                "intents": self.intents,
            },
        )

        self.heartbeat_interval = int(
            payload.data['heartbeat_interval'] / 1000
        )

        if not self.heartbeat_task or self.heartbeat_task.cancelled():
            self.heartbeat_task = asyncio.ensure_future(
                self.handle_heartbeat_task()
            )


    async def start_connection(self) -> None:
        """
            |coro|
            This function is used to start the connection.
            It do connect to the gateway and start the event handling.
        """
        for i in itertools.count():
            try:
                self.websocket = await self.session.ws_connect(
                    self.make_url(),
                )
                break
            except aiohttp.ClientConnectorError:
                logger.warning(
                    f" {self.shard_id} Failed to connect to gateway, retrying in 5 seconds..."
                )

                await asyncio.sleep(5)

        await self.start_event_handling()

    async def handle_message(self, message: aiohttp.ClientWebSocketResponse):
        """
            |coro|
            This is the handler for the message that come from the websocket
        """
        if message.type == aiohttp.WSMsgType.TEXT:
            await self.handle_data(message.data)
        elif message.type == aiohttp.WSMsgType.BINARY:
            data = self.decompress(message.data)
            if data is None:
                return None
            await self.handle_data(data)
        elif message.type == aiohttp.WSMsgType.ERROR:
            logger.warning(
                f" {self.shard_id} Websocket error: {message.exception()}"
            )

        await self.handle_error(self.websocket.close_code)

    async def handle_error(self, code: int):
        """
            |coro|
            This is the handler for the error that come from the websocket
        """

        error = self.__errors.get(code, None)

        if error is not None:
            raise error

            
    async def start_event_handling(self):
        """
            |coro|
            This function is the responsible of handling the event and praseing the data
        """
        async for message in self.websocket:
            await self.handle_message(message)

    async def handle_data(self, data: str):
        """
            |coro|
            This function is the handler for the data that come from the websocket.
        """
        payload = GatewayDispatch.form(data)

        if payload.seq is not None:
            self.sequence = payload.seq

        asyncio.ensure_future(
            self.__handler.get(payload.op)(payload)
        )

    async def handle_hello(self, payload: GatewayDispatch):
        """
            |coro|
            This function is the handler for the hello opcode.
        """

        logger.info(
            f" {self.shard_id} Connected to gateway"
        )

        await self.send_identify(payload)

    async def handle_reconnect(self, payload: GatewayDispatch):
        """
            |coro|
            This function is the handler for the reconnect opcode.
        """
        logger.debug(
            f" {self.shard_id} Reconnecting to gateway..."
        )

        self.should_reconnect = True

        await self.start_connection()

    async def handle_invalid_session(self, payload: GatewayDispatch):
        """
            |coro|
            This function is the handler for the invalid session opcode.
        """
        logger.warning(
            f" {self.shard_id} Invalid session, reconnecting..."
        )

        await asyncio.sleep(5)

        self.should_reconnect = False

        await self.start_connection()

    async def handle_heartbeat_ack(self, payload: GatewayDispatch):
        """
            |coro|
            This function is the handler for the heartbeat opcode.
        """
        if not self.heartbeat_ack:
            logger.debug(
                f" {self.shard_id} Received heartbeat ack"
            )

            self.heartbeat_ack = True

    async def handle_heartbeat_task(self):
        """
            |coro|
            This function is the handler for the heartbeat task.
        """
        while True:
            await asyncio.sleep(self.heartbeat_interval)
            
            await self.send(1, self.sequence)

            logger.debug(
                f" {self.shard_id} Heartbeat sent to gateway..."
            )