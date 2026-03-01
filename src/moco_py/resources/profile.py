"""Profile resource."""

from __future__ import annotations

from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.profile import Profile


class ProfileResource(SyncResource):
    """Synchronous profile resource."""

    def get(self) -> MocoResponse[Profile]:
        """Retrieve the current user's profile."""
        return self._get("/profile", cast_to=Profile)


class AsyncProfileResource(AsyncResource):
    """Asynchronous profile resource."""

    async def get(self) -> MocoResponse[Profile]:
        """Retrieve the current user's profile."""
        return await self._get("/profile", cast_to=Profile)
