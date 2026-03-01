"""Project Tasks resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.project_tasks import ProjectTask


class ProjectTasks(SyncResource):
    """Synchronous project tasks resource."""

    def list(self, project_id: int) -> SyncPage[ProjectTask]:
        """Retrieve all tasks on a project."""
        return self._get_list(f"/projects/{project_id}/tasks", cast_to=ProjectTask)

    def get(self, project_id: int, task_id: int) -> MocoResponse[ProjectTask]:
        """Retrieve a single task on a project."""
        return self._get(f"/projects/{project_id}/tasks/{task_id}", cast_to=ProjectTask)

    def create(
        self,
        project_id: int,
        *,
        name: str,
        billable: bool | None = None,
        active: bool | None = None,
        budget: float | None = None,
        hourly_rate: float | None = None,
        description: str | None = None,
    ) -> MocoResponse[ProjectTask]:
        """Create a task on a project."""
        data: dict[str, Any] = {"name": name}
        if billable is not None:
            data["billable"] = billable
        if active is not None:
            data["active"] = active
        if budget is not None:
            data["budget"] = budget
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        if description is not None:
            data["description"] = description
        return self._post(
            f"/projects/{project_id}/tasks",
            json_data=data,
            cast_to=ProjectTask,
        )

    def update(
        self,
        project_id: int,
        task_id: int,
        *,
        name: str | None = None,
        billable: bool | None = None,
        active: bool | None = None,
        budget: float | None = None,
        hourly_rate: float | None = None,
        description: str | None = None,
    ) -> MocoResponse[ProjectTask]:
        """Update a task on a project."""
        data: dict[str, Any] = {}
        if name is not None:
            data["name"] = name
        if billable is not None:
            data["billable"] = billable
        if active is not None:
            data["active"] = active
        if budget is not None:
            data["budget"] = budget
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        if description is not None:
            data["description"] = description
        return self._put(
            f"/projects/{project_id}/tasks/{task_id}",
            json_data=data,
            cast_to=ProjectTask,
        )

    def delete(self, project_id: int, task_id: int) -> MocoResponse[None]:
        """Delete a task on a project."""
        return self._delete(f"/projects/{project_id}/tasks/{task_id}")

    def destroy_all(self, project_id: int) -> MocoResponse[None]:
        """Delete all deletable tasks on a project."""
        return self._delete(f"/projects/{project_id}/tasks/destroy_all")


class AsyncProjectTasks(AsyncResource):
    """Asynchronous project tasks resource."""

    async def list(self, project_id: int) -> AsyncPage[ProjectTask]:
        """Retrieve all tasks on a project."""
        return await self._get_list(
            f"/projects/{project_id}/tasks", cast_to=ProjectTask
        )

    async def get(self, project_id: int, task_id: int) -> MocoResponse[ProjectTask]:
        """Retrieve a single task on a project."""
        return await self._get(
            f"/projects/{project_id}/tasks/{task_id}", cast_to=ProjectTask
        )

    async def create(
        self,
        project_id: int,
        *,
        name: str,
        billable: bool | None = None,
        active: bool | None = None,
        budget: float | None = None,
        hourly_rate: float | None = None,
        description: str | None = None,
    ) -> MocoResponse[ProjectTask]:
        """Create a task on a project."""
        data: dict[str, Any] = {"name": name}
        if billable is not None:
            data["billable"] = billable
        if active is not None:
            data["active"] = active
        if budget is not None:
            data["budget"] = budget
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        if description is not None:
            data["description"] = description
        return await self._post(
            f"/projects/{project_id}/tasks",
            json_data=data,
            cast_to=ProjectTask,
        )

    async def update(
        self,
        project_id: int,
        task_id: int,
        *,
        name: str | None = None,
        billable: bool | None = None,
        active: bool | None = None,
        budget: float | None = None,
        hourly_rate: float | None = None,
        description: str | None = None,
    ) -> MocoResponse[ProjectTask]:
        """Update a task on a project."""
        data: dict[str, Any] = {}
        if name is not None:
            data["name"] = name
        if billable is not None:
            data["billable"] = billable
        if active is not None:
            data["active"] = active
        if budget is not None:
            data["budget"] = budget
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        if description is not None:
            data["description"] = description
        return await self._put(
            f"/projects/{project_id}/tasks/{task_id}",
            json_data=data,
            cast_to=ProjectTask,
        )

    async def delete(self, project_id: int, task_id: int) -> MocoResponse[None]:
        """Delete a task on a project."""
        return await self._delete(f"/projects/{project_id}/tasks/{task_id}")

    async def destroy_all(self, project_id: int) -> MocoResponse[None]:
        """Delete all deletable tasks on a project."""
        return await self._delete(f"/projects/{project_id}/tasks/destroy_all")
