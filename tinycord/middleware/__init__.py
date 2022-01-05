import typing
import os

from glob import glob
from pathlib import Path
from importlib import import_module

def get_middlewares() -> typing.Dict[str, typing.Union[typing.Callable, typing.Awaitable]]:
    """
        This function is used to get all the middlewares. from the middleware folder.
    """
    middlewares: typing.Dict[str, typing.Union[typing.Callable, typing.Awaitable]] = {}
    """ The middlewares of the bot. """


    with Path(__file__).parent.resolve() as path:

        for file in glob(os.path.abspath(path) + "\*.py"):

            event = file.split('/')[-1].split('.')[0].split(u'\u005c')[-1]
            """ The event of the middleware. """

            try:
                module: module = import_module(f".{event}", package=__name__)
                """ The module of the middleware. """
                middlewares[event] = getattr(module, 'export')()
                """ The middleware of the bot. """

            except ModuleNotFoundError:
                continue
            except AttributeError:
                continue

        return middlewares
        """ The middlewares of the bot. """