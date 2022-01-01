import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from ..mixins import Hashable
from ...utils import Snowflake
from .user import User

@dataclasses.dataclass(repr=False)
class Integration(Hashable):
    """
        This is the User it used to represent a integration.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the integration. 
    """
    def __init__(self, client: "Client", **data) -> None:
        self.client = client
        """The main client."""

        self.id: Snowflake = Snowflake(
            data.get('id'))
        """The ID of the integration."""

        self.name: str = data.get('name')
        """The name of the integration."""

        self.type: str = data.get('type')
        """The type of the integration."""

        self.enabled: bool = data.get('enabled')
        """Whether the integration is enabled or not."""

        self.syncing: typing.Union[bool, None] = data.get('syncing')
        """Whether the integration is syncing or not."""

        self.role_id: typing.Union[Snowflake, None] = data.get('role_id')
        """The role ID of the integration."""

        self.expire_behavior: typing.Union[int, None] = data.get('expire_behavior')
        """The expire behavior of the integration."""

        self.expire_grace_period: typing.Union[int, None] = data.get('expire_grace_period')
        """The expire grace period of the integration."""

        self.user: typing.Union["User", None] = User(self.client, **data.get('user')) if data.get('user') else None
        """The user of the integration."""

        self.account: typing.Dict[str, str] = data.get('account')
        """The account of the integration."""

        self.synced_at: typing.Union[int, None] = data.get('synced_at')
        """The synced at of the integration."""
        
        self.subscriber_count: typing.Union[int, None] = data.get('subscriber_count')
        """The subscriber count of the integration."""
        
        self.revoked: typing.Union[bool, None] = data.get('revoked')
        """Whether the integration is revoked or not."""
        
        self.applications: typing.List[typing.Dict[str, str]] = data.get('applications')
        """The applications of the integration."""