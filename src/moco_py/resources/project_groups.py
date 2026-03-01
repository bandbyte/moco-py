"""Project Groups resource."""

from __future__ import annotations

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.project_groups import ProjectGroup


class ProjectGroups(SyncResource):
    """Synchronous project groups resource."""

    def list(self) -> SyncPage[ProjectGroup]:
        """Retrieve all project groups."""
        return self._get_list("/projects/groups", cast_to=ProjectGroup)

    def get(self, project_group_id: int) -> MocoResponse[ProjectGroup]:
        """Retrieve a single project group."""
        return self._get(f"/projects/groups/{project_group_id}", cast_to=ProjectGroup)


class AsyncProjectGroups(AsyncResource):
    """Asynchronous project groups resource."""

    async def list(self) -> AsyncPage[ProjectGroup]:
        """Retrieve all project groups."""
        return await self._get_list("/projects/groups", cast_to=ProjectGroup)

    async def get(self, project_group_id: int) -> MocoResponse[ProjectGroup]:
        """Retrieve a single project group."""
        return await self._get(
            f"/projects/groups/{project_group_id}", cast_to=ProjectGroup
        )
