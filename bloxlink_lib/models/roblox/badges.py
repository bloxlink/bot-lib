from bloxlink_lib.fetch import fetch_typed
from bloxlink_lib.models.base import BaseModel
from .base import get_entity
from .base_assets import RobloxBaseAsset


BADGE_API = "https://badges.roblox.com/v1/badges"


class RobloxBadgeResponse(BaseModel):
    """Representation of the response from the Roblox badge API."""

    id: int
    name: str
    description: str | None


class RobloxBadge(RobloxBaseAsset):
    """Representation of a Badge on Roblox."""

    type: str = "badge"

    async def sync(self):
        """Load badge data from Roblox"""

        if self.synced:
            return

        badge_data, _ = await fetch_typed(RobloxBadgeResponse, f"{BADGE_API}/{self.id}")

        self.name = badge_data.name
        self.description = badge_data.description

        self.synced = True


async def get_badge(badge_id: int) -> RobloxBadge:
    """Wrapper around get_entity() to get and sync a badge from Roblox.

    Args:
        badge_id (int): ID of the badge.

    Returns:
        RobloxBadge: A synced roblox badge.
    """

    return await get_entity("badge", badge_id)
