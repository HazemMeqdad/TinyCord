# TinyCord is a discord bot written in python.
# LICENSE: MIT
# AUTHOR: xArty

from __future__ import annotations

import typing
import logging
import asyncio
import logging

if typing.TYPE_CHECKING:
    from .intents import Intents
    from .models import *

from .core import Gateway, HTTPClient, GatewayDispatch
from .middleware import get_middlewares
from .utils import Snowflake

logger: logging.Logger = logging.Logger("tinycord")
events: typing.List[typing.Coroutine] = {}

def middleware_event(event: str):
    """
        This function is used to register a middleware event.
        This is used to register events that are called before the event is called.
        
        Usage: 
        ```
        @middleware_event("ready")
        def my_middleware(gatway, event):
            return "on_ready", [
                event
            ]

        @client.event
        def on_ready(event):
            print("Ready!")
        ```
            
    """
    def decorator(func: typing.Awaitable):
        
        async def warpper(cls, *args, **kwargs):
            return await func(cls, *args, **kwargs)
        
        events[event] = warpper
        return warpper
    return decorator

for event, ware in get_middlewares().items():
    """
        This function is used to register a middleware event.
        This is used to register middlewares before anything happens.
    """
    middleware_event(event)(ware)

class Client:
    """
        The bridge between Python and Discord API.
        This is the main class that is used to connect to Discord.

        Example:
            client = Client()

            @client.event
            async def on_ready():
                print("Ready!")

            client.run(token)
    """
    def __init__(
        self,
        token: str,
        *,
        bot: bool = True,
        intents: typing.List[Intents],
        reconnect: bool = True,
    ) -> None:
        self.token = f'Bot {token}' if bot is True else token
        """ The token of the bot. """

        self.intents = sum([int(i) for i in intents])
        """ The intents of the bot. """

        self.bot = bot
        """ Whether the bot is a bot or not. """

        self.reconnect = reconnect
        """ Whether the bot should reconnect or not. """

        self.loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        """ The event loop of the bot. """

        self.http = HTTPClient(self)
        """ The HTTP client of the bot. """

        self.user: "User" = None
        """ The user of the bot. """

        self.messages: typing.Dict[str, "Message"] = {}
        """ The messages of the bot. """

        self.guilds: typing.Dict[str, "Guild"] = {}
        """ The guilds of the bot. """

        self.channels: typing.Dict[str, "All"] = {}
        """ The channels of the bot. """

        self.threads: typing.Dict[str, "ThreadChannel"] = {}
        """ The threads of the bot. """

        self.users: typing.Dict[str, "User"] = {}
        """ The users of the bot. """

    @classmethod
    def event(cls, func: typing.Callable) -> typing.Union[typing.Callable, typing.Awaitable]:
        """
            This function is used to register an event.
            This is used to register events that are called after the event is called.
        """

        events[func.__name__] = func

        return func

    @classmethod
    def listen(cls, event: str) -> typing.Union[typing.Callable, typing.Awaitable]:
        """
            This function is used to register an event.
            This is used to register events that are called after the event is called.
        """

        def decorator(func: typing.Callable):
            events[event] = 'on_' + event

            return func
        return decorator

    def connect(self) -> None:
        """
            This function is used to connect to Discord.
        """
        asyncio.ensure_future(self.start_shard(0, 1), loop = self.loop)

        logger.info("Connecting to Discord...")

        self.loop.run_forever()

    def connect_autosharded(self) -> None:
        """
            This function is used to connect to Discord with autosharding.
        """
        self.info = self.loop.run_until_complete(self.http.request('/gateway/bot', 'GET'))

        for shard in range(self.info['shards']):

            asyncio.ensure_future(
                self.start_shard(shard, self.info['shards']),
                loop = self.loop,
            )
            
            self.loop.run_forever()

    async def start_shard(
        self,
        shard_id: int,
        shard_count: int,
    ) -> None:
        """
            This function is used to start a shard.
        """

        url = await self.http.request('/gateway', 'GET')
        
        self.gw = gateway = Gateway(
            token = self.token,
            intents = self.intents,
            url = url['url'],
            shard_id = shard_id,
            shard_count = shard_count,
        )

        self.gw.append_handler({
            0: self.handle_event,
        })

        asyncio.create_task(gateway.start_connection())

    async def handle_middleware(self, client: "Client", gateway: "Gateway" , payload: "GatewayDispatch") -> None:
        """
            This function is used to handle middleware events.
            It's called before the event is called. Which means that you can modify the event.
            It's very useful for thing like event handling and event praseing.
        """
        event = payload.event.lower()
        ware = events.get(event,None)

        if ware is not None:
            extractable = await ware(client, gateway, payload)

            logger.debug(f"Middleware {event} has been called.")

            if not isinstance(extractable, tuple):
                raise RuntimeError(
                    f"Return type from `{event}` middleware must be tuple. "
                )

            event = extractable[0]
            args = extractable[1]

            callback = events.get(event, None)

            return (event, args, callback)

        return (None, None, None)

    async def handle_event(self, payload: "GatewayDispatch") -> None:
        """
            This function is used to handle an event.
            It's called after the middleware is called.
        """
        event, args, callback = await self.handle_middleware(self, self.gw, payload)
        
        if callback != None:
            await callback(*args)

    def get_user(self, id: Snowflake) -> typing.Union["User", None]:
        """Get a user of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the user.

        Returns
        -------
        :class:`User`
            The user of the guild.
        """

        return self.users.get(str(id), None)

    def get_channel(self, id: Snowflake) -> typing.Union["All", None]:
        """Get a channel of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the channel.

        Returns
        -------
        :class:`All`
            The channel of the guild.
        """

        return self.channels.get(str(id), None)

    def get_thread(self, id: Snowflake) -> typing.Union["ThreadChannel", None]:
        """Get a thread of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the thread.

        Returns
        -------
        :class:`TextChannel`
            The thread of the guild.
        """

        return self.threads.get(str(id), None)

    def get_message(self, id: Snowflake) -> typing.Union["Message", None]:
        """Get a message of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the message.

        Returns
        -------
        :class:`Message`
            The message of the guild.
        """

        return self.messages.get(str(id), None)