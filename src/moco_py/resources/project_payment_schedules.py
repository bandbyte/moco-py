"""Project Payment Schedules resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.project_payment_schedules import ProjectPaymentSchedule


class ProjectPaymentSchedules(SyncResource):
    """Synchronous project payment schedules resource."""

    def list(
        self,
        project_id: int,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        checked: bool | None = None,
    ) -> SyncPage[ProjectPaymentSchedule]:
        """Retrieve all payment schedules for a project."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if checked is not None:
            params["checked"] = checked
        return self._get_list(
            f"/projects/{project_id}/payment_schedules",
            params=params or None,
            cast_to=ProjectPaymentSchedule,
        )

    def list_all(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        checked: bool | None = None,
        company_id: int | None = None,
        project_id: int | None = None,
        sort_by: str | None = None,
    ) -> SyncPage[ProjectPaymentSchedule]:
        """Retrieve all payment schedules independent of a project."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if checked is not None:
            params["checked"] = checked
        if company_id is not None:
            params["company_id"] = company_id
        if project_id is not None:
            params["project_id"] = project_id
        if sort_by is not None:
            params["sort_by"] = sort_by
        return self._get_list(
            "/projects/payment_schedules",
            params=params or None,
            cast_to=ProjectPaymentSchedule,
        )

    def get(
        self, project_id: int, payment_schedule_id: int
    ) -> MocoResponse[ProjectPaymentSchedule]:
        """Retrieve a single payment schedule on a project."""
        return self._get(
            f"/projects/{project_id}/payment_schedules/{payment_schedule_id}",
            cast_to=ProjectPaymentSchedule,
        )

    def create(
        self,
        project_id: int,
        *,
        net_total: float,
        date: str,
        title: str | None = None,
        checked: bool | None = None,
    ) -> MocoResponse[ProjectPaymentSchedule]:
        """Create a payment schedule for a project."""
        data: dict[str, Any] = {"net_total": net_total, "date": date}
        if title is not None:
            data["title"] = title
        if checked is not None:
            data["checked"] = checked
        return self._post(
            f"/projects/{project_id}/payment_schedules",
            json_data=data,
            cast_to=ProjectPaymentSchedule,
        )

    def update(
        self,
        project_id: int,
        payment_schedule_id: int,
        *,
        net_total: float | None = None,
        date: str | None = None,
        title: str | None = None,
        checked: bool | None = None,
    ) -> MocoResponse[ProjectPaymentSchedule]:
        """Update a payment schedule for a project."""
        data: dict[str, Any] = {}
        if net_total is not None:
            data["net_total"] = net_total
        if date is not None:
            data["date"] = date
        if title is not None:
            data["title"] = title
        if checked is not None:
            data["checked"] = checked
        return self._put(
            f"/projects/{project_id}/payment_schedules/{payment_schedule_id}",
            json_data=data,
            cast_to=ProjectPaymentSchedule,
        )

    def delete(self, project_id: int, payment_schedule_id: int) -> MocoResponse[None]:
        """Delete a payment schedule."""
        return self._delete(
            f"/projects/{project_id}/payment_schedules/{payment_schedule_id}"
        )


class AsyncProjectPaymentSchedules(AsyncResource):
    """Asynchronous project payment schedules resource."""

    async def list(
        self,
        project_id: int,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        checked: bool | None = None,
    ) -> AsyncPage[ProjectPaymentSchedule]:
        """Retrieve all payment schedules for a project."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if checked is not None:
            params["checked"] = checked
        return await self._get_list(
            f"/projects/{project_id}/payment_schedules",
            params=params or None,
            cast_to=ProjectPaymentSchedule,
        )

    async def list_all(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        checked: bool | None = None,
        company_id: int | None = None,
        project_id: int | None = None,
        sort_by: str | None = None,
    ) -> AsyncPage[ProjectPaymentSchedule]:
        """Retrieve all payment schedules independent of a project."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if checked is not None:
            params["checked"] = checked
        if company_id is not None:
            params["company_id"] = company_id
        if project_id is not None:
            params["project_id"] = project_id
        if sort_by is not None:
            params["sort_by"] = sort_by
        return await self._get_list(
            "/projects/payment_schedules",
            params=params or None,
            cast_to=ProjectPaymentSchedule,
        )

    async def get(
        self, project_id: int, payment_schedule_id: int
    ) -> MocoResponse[ProjectPaymentSchedule]:
        """Retrieve a single payment schedule on a project."""
        return await self._get(
            f"/projects/{project_id}/payment_schedules/{payment_schedule_id}",
            cast_to=ProjectPaymentSchedule,
        )

    async def create(
        self,
        project_id: int,
        *,
        net_total: float,
        date: str,
        title: str | None = None,
        checked: bool | None = None,
    ) -> MocoResponse[ProjectPaymentSchedule]:
        """Create a payment schedule for a project."""
        data: dict[str, Any] = {"net_total": net_total, "date": date}
        if title is not None:
            data["title"] = title
        if checked is not None:
            data["checked"] = checked
        return await self._post(
            f"/projects/{project_id}/payment_schedules",
            json_data=data,
            cast_to=ProjectPaymentSchedule,
        )

    async def update(
        self,
        project_id: int,
        payment_schedule_id: int,
        *,
        net_total: float | None = None,
        date: str | None = None,
        title: str | None = None,
        checked: bool | None = None,
    ) -> MocoResponse[ProjectPaymentSchedule]:
        """Update a payment schedule for a project."""
        data: dict[str, Any] = {}
        if net_total is not None:
            data["net_total"] = net_total
        if date is not None:
            data["date"] = date
        if title is not None:
            data["title"] = title
        if checked is not None:
            data["checked"] = checked
        return await self._put(
            f"/projects/{project_id}/payment_schedules/{payment_schedule_id}",
            json_data=data,
            cast_to=ProjectPaymentSchedule,
        )

    async def delete(
        self, project_id: int, payment_schedule_id: int
    ) -> MocoResponse[None]:
        """Delete a payment schedule."""
        return await self._delete(
            f"/projects/{project_id}/payment_schedules/{payment_schedule_id}"
        )
