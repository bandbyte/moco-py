"""User Permission Roles resource."""

from __future__ import annotations

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from ..types.user_roles import UserRole


class UserRoles(SyncResource):
    """Synchronous user roles resource."""

    def list(self) -> SyncPage[UserRole]:
        """Retrieve all user roles."""
        return self._get_list("/users/roles", cast_to=UserRole)


class AsyncUserRoles(AsyncResource):
    """Asynchronous user roles resource."""

    async def list(self) -> AsyncPage[UserRole]:
        """Retrieve all user roles."""
        return await self._get_list("/users/roles", cast_to=UserRole)
