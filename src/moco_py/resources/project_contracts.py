"""Project Contracts resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.project_contracts import ProjectContract


class ProjectContracts(SyncResource):
    """Synchronous project contracts resource."""

    def list(self, project_id: int) -> SyncPage[ProjectContract]:
        """Retrieve all staff assignments for a project."""
        return self._get_list(
            f"/projects/{project_id}/contracts", cast_to=ProjectContract
        )

    def get(self, project_id: int, contract_id: int) -> MocoResponse[ProjectContract]:
        """Retrieve a single staff assignment on a project."""
        return self._get(
            f"/projects/{project_id}/contracts/{contract_id}",
            cast_to=ProjectContract,
        )

    def create(
        self,
        project_id: int,
        *,
        user_id: int,
        billable: bool | None = None,
        active: bool | None = None,
        budget: float | None = None,
        hourly_rate: float | None = None,
    ) -> MocoResponse[ProjectContract]:
        """Assign a person to a project."""
        data: dict[str, Any] = {"user_id": user_id}
        if billable is not None:
            data["billable"] = billable
        if active is not None:
            data["active"] = active
        if budget is not None:
            data["budget"] = budget
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        return self._post(
            f"/projects/{project_id}/contracts",
            json_data=data,
            cast_to=ProjectContract,
        )

    def update(
        self,
        project_id: int,
        contract_id: int,
        *,
        billable: bool | None = None,
        active: bool | None = None,
        budget: float | None = None,
        hourly_rate: float | None = None,
    ) -> MocoResponse[ProjectContract]:
        """Update a staff assignment on a project."""
        data: dict[str, Any] = {}
        if billable is not None:
            data["billable"] = billable
        if active is not None:
            data["active"] = active
        if budget is not None:
            data["budget"] = budget
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        return self._put(
            f"/projects/{project_id}/contracts/{contract_id}",
            json_data=data,
            cast_to=ProjectContract,
        )

    def delete(self, project_id: int, contract_id: int) -> MocoResponse[None]:
        """Delete a staff assignment on a project."""
        return self._delete(f"/projects/{project_id}/contracts/{contract_id}")


class AsyncProjectContracts(AsyncResource):
    """Asynchronous project contracts resource."""

    async def list(self, project_id: int) -> AsyncPage[ProjectContract]:
        """Retrieve all staff assignments for a project."""
        return await self._get_list(
            f"/projects/{project_id}/contracts", cast_to=ProjectContract
        )

    async def get(
        self, project_id: int, contract_id: int
    ) -> MocoResponse[ProjectContract]:
        """Retrieve a single staff assignment on a project."""
        return await self._get(
            f"/projects/{project_id}/contracts/{contract_id}",
            cast_to=ProjectContract,
        )

    async def create(
        self,
        project_id: int,
        *,
        user_id: int,
        billable: bool | None = None,
        active: bool | None = None,
        budget: float | None = None,
        hourly_rate: float | None = None,
    ) -> MocoResponse[ProjectContract]:
        """Assign a person to a project."""
        data: dict[str, Any] = {"user_id": user_id}
        if billable is not None:
            data["billable"] = billable
        if active is not None:
            data["active"] = active
        if budget is not None:
            data["budget"] = budget
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        return await self._post(
            f"/projects/{project_id}/contracts",
            json_data=data,
            cast_to=ProjectContract,
        )

    async def update(
        self,
        project_id: int,
        contract_id: int,
        *,
        billable: bool | None = None,
        active: bool | None = None,
        budget: float | None = None,
        hourly_rate: float | None = None,
    ) -> MocoResponse[ProjectContract]:
        """Update a staff assignment on a project."""
        data: dict[str, Any] = {}
        if billable is not None:
            data["billable"] = billable
        if active is not None:
            data["active"] = active
        if budget is not None:
            data["budget"] = budget
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        return await self._put(
            f"/projects/{project_id}/contracts/{contract_id}",
            json_data=data,
            cast_to=ProjectContract,
        )

    async def delete(self, project_id: int, contract_id: int) -> MocoResponse[None]:
        """Delete a staff assignment on a project."""
        return await self._delete(f"/projects/{project_id}/contracts/{contract_id}")
