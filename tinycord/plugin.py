import asyncio
import collections
import typing

if typing.TYPE_CHECKING:
    from .client import Client

class Plugin:
    """
        This class is used to create a plugin. that sprites the events between multiple files.
        Something like cogs in discord.py and picner but more reliable.

        Parameters
        ----------
        name : `str`
            The name of the plugin.
        
        Attributes
        ----------
        name : `str`
            The name of the plugin.
        loop : `asyncio.AbstractEventLoop`
            The event loop.
    """
    def __init__(self, name: str) -> None:
        self.name: str = name
        """The name of the plugin."""

        self.loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        """The event loop."""

        self.client: "Client" = None
        """The client."""

        self.events: typing.Dict[str, typing.List[typing.Awaitable]] = collections.defaultdict(list)

    def event(self, func: typing.Callable) -> typing.Union[typing.Callable, typing.Awaitable]:
        """
            This function is used to register an event.
            This is used to register events that are called after the event is called.
            
            Parameters
            ----------
            func : `typing.Callable`
                The function to register.
        """

        self.events[func.__name__].append(func)

        return func

    def listen(self, event: str) -> typing.Union[typing.Callable, typing.Awaitable]:
        """
            This function is used to register an event.
            This is used to register events that are called after the event is called.

            Parameters
            ----------
            event : `str`
                The event to listen for.
        """
        def decorator(func: typing.Callable):
            self.events[event].append(func)

            return func
        return decorator

