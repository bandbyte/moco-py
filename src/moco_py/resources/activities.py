"""Activities resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import RemoteService
from ..types.activities import Activity


class Activities(SyncResource):
    """Synchronous activities resource."""

    def list(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        user_id: int | None = None,
        project_id: int | None = None,
        task_id: int | None = None,
        company_id: int | None = None,
        billable: bool | None = None,
        billed: bool | None = None,
        term: str | None = None,
    ) -> SyncPage[Activity]:
        """Retrieve all activities."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if user_id is not None:
            params["user_id"] = user_id
        if project_id is not None:
            params["project_id"] = project_id
        if task_id is not None:
            params["task_id"] = task_id
        if company_id is not None:
            params["company_id"] = company_id
        if billable is not None:
            params["billable"] = billable
        if billed is not None:
            params["billed"] = billed
        if term is not None:
            params["term"] = term
        return self._get_list("/activities", params=params, cast_to=Activity)

    def get(self, activity_id: int) -> MocoResponse[Activity]:
        """Retrieve a single activity."""
        return self._get(f"/activities/{activity_id}", cast_to=Activity)

    def create(
        self,
        *,
        date: str,
        project_id: int,
        task_id: int,
        seconds: int | None = None,
        description: str | None = None,
        billable: bool | None = None,
        tag: str | None = None,
        remote_service: RemoteService | None = None,
        remote_id: str | None = None,
        remote_url: str | None = None,
    ) -> MocoResponse[Activity]:
        """Create an activity."""
        data: dict[str, Any] = {
            "date": date,
            "project_id": project_id,
            "task_id": task_id,
        }
        if seconds is not None:
            data["seconds"] = seconds
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if tag is not None:
            data["tag"] = tag
        if remote_service is not None:
            data["remote_service"] = remote_service
        if remote_id is not None:
            data["remote_id"] = remote_id
        if remote_url is not None:
            data["remote_url"] = remote_url
        return self._post("/activities", json_data=data, cast_to=Activity)

    def bulk_create(
        self,
        *,
        activities: list[dict[str, Any]],  # type: ignore[valid-type]
    ) -> MocoResponse[list[Activity]]:  # type: ignore[valid-type]
        """Bulk insert activities."""
        return self._transport.request(
            "POST",
            "/activities/bulk",
            json_data={"activities": activities},
            cast_to=Activity,
            is_list=True,
        )

    def update(
        self,
        activity_id: int,
        *,
        date: str | None = None,
        project_id: int | None = None,
        task_id: int | None = None,
        seconds: int | None = None,
        description: str | None = None,
        billable: bool | None = None,
        tag: str | None = None,
        remote_service: RemoteService | None = None,
        remote_id: str | None = None,
        remote_url: str | None = None,
    ) -> MocoResponse[Activity]:
        """Update an activity."""
        data: dict[str, Any] = {}
        if date is not None:
            data["date"] = date
        if project_id is not None:
            data["project_id"] = project_id
        if task_id is not None:
            data["task_id"] = task_id
        if seconds is not None:
            data["seconds"] = seconds
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if tag is not None:
            data["tag"] = tag
        if remote_service is not None:
            data["remote_service"] = remote_service
        if remote_id is not None:
            data["remote_id"] = remote_id
        if remote_url is not None:
            data["remote_url"] = remote_url
        return self._put(f"/activities/{activity_id}", json_data=data, cast_to=Activity)

    def delete(self, activity_id: int) -> MocoResponse[None]:
        """Delete an activity."""
        return self._delete(f"/activities/{activity_id}")

    def start_timer(self, activity_id: int) -> MocoResponse[Activity]:
        """Start or continue a timer on an activity."""
        return self._patch(f"/activities/{activity_id}/start_timer", cast_to=Activity)

    def stop_timer(self, activity_id: int) -> MocoResponse[Activity]:
        """Stop a timer running on an activity."""
        return self._patch(f"/activities/{activity_id}/stop_timer", cast_to=Activity)

    def disregard(
        self,
        *,
        reason: str,
        activity_ids: list[int],  # type: ignore[valid-type]
        company_id: int,
        project_id: int | None = None,
    ) -> MocoResponse[None]:
        """Mark activities as already billed."""
        data: dict[str, Any] = {
            "reason": reason,
            "activity_ids": activity_ids,
            "company_id": company_id,
        }
        if project_id is not None:
            data["project_id"] = project_id
        return self._post(
            "/activities/disregard",
            json_data=data,
            cast_to=None,  # type: ignore[arg-type]
        )


class AsyncActivities(AsyncResource):
    """Asynchronous activities resource."""

    async def list(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        user_id: int | None = None,
        project_id: int | None = None,
        task_id: int | None = None,
        company_id: int | None = None,
        billable: bool | None = None,
        billed: bool | None = None,
        term: str | None = None,
    ) -> AsyncPage[Activity]:
        """Retrieve all activities."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if user_id is not None:
            params["user_id"] = user_id
        if project_id is not None:
            params["project_id"] = project_id
        if task_id is not None:
            params["task_id"] = task_id
        if company_id is not None:
            params["company_id"] = company_id
        if billable is not None:
            params["billable"] = billable
        if billed is not None:
            params["billed"] = billed
        if term is not None:
            params["term"] = term
        return await self._get_list("/activities", params=params, cast_to=Activity)

    async def get(self, activity_id: int) -> MocoResponse[Activity]:
        """Retrieve a single activity."""
        return await self._get(f"/activities/{activity_id}", cast_to=Activity)

    async def create(
        self,
        *,
        date: str,
        project_id: int,
        task_id: int,
        seconds: int | None = None,
        description: str | None = None,
        billable: bool | None = None,
        tag: str | None = None,
        remote_service: RemoteService | None = None,
        remote_id: str | None = None,
        remote_url: str | None = None,
    ) -> MocoResponse[Activity]:
        """Create an activity."""
        data: dict[str, Any] = {
            "date": date,
            "project_id": project_id,
            "task_id": task_id,
        }
        if seconds is not None:
            data["seconds"] = seconds
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if tag is not None:
            data["tag"] = tag
        if remote_service is not None:
            data["remote_service"] = remote_service
        if remote_id is not None:
            data["remote_id"] = remote_id
        if remote_url is not None:
            data["remote_url"] = remote_url
        return await self._post("/activities", json_data=data, cast_to=Activity)

    async def bulk_create(
        self,
        *,
        activities: list[dict[str, Any]],  # type: ignore[valid-type]
    ) -> MocoResponse[list[Activity]]:  # type: ignore[valid-type]
        """Bulk insert activities."""
        return await self._transport.request(
            "POST",
            "/activities/bulk",
            json_data={"activities": activities},
            cast_to=Activity,
            is_list=True,
        )

    async def update(
        self,
        activity_id: int,
        *,
        date: str | None = None,
        project_id: int | None = None,
        task_id: int | None = None,
        seconds: int | None = None,
        description: str | None = None,
        billable: bool | None = None,
        tag: str | None = None,
        remote_service: RemoteService | None = None,
        remote_id: str | None = None,
        remote_url: str | None = None,
    ) -> MocoResponse[Activity]:
        """Update an activity."""
        data: dict[str, Any] = {}
        if date is not None:
            data["date"] = date
        if project_id is not None:
            data["project_id"] = project_id
        if task_id is not None:
            data["task_id"] = task_id
        if seconds is not None:
            data["seconds"] = seconds
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if tag is not None:
            data["tag"] = tag
        if remote_service is not None:
            data["remote_service"] = remote_service
        if remote_id is not None:
            data["remote_id"] = remote_id
        if remote_url is not None:
            data["remote_url"] = remote_url
        return await self._put(
            f"/activities/{activity_id}", json_data=data, cast_to=Activity
        )

    async def delete(self, activity_id: int) -> MocoResponse[None]:
        """Delete an activity."""
        return await self._delete(f"/activities/{activity_id}")

    async def start_timer(self, activity_id: int) -> MocoResponse[Activity]:
        """Start or continue a timer on an activity."""
        return await self._patch(
            f"/activities/{activity_id}/start_timer", cast_to=Activity
        )

    async def stop_timer(self, activity_id: int) -> MocoResponse[Activity]:
        """Stop a timer running on an activity."""
        return await self._patch(
            f"/activities/{activity_id}/stop_timer", cast_to=Activity
        )

    async def disregard(
        self,
        *,
        reason: str,
        activity_ids: list[int],  # type: ignore[valid-type]
        company_id: int,
        project_id: int | None = None,
    ) -> MocoResponse[None]:
        """Mark activities as already billed."""
        data: dict[str, Any] = {
            "reason": reason,
            "activity_ids": activity_ids,
            "company_id": company_id,
        }
        if project_id is not None:
            data["project_id"] = project_id
        return await self._post(
            "/activities/disregard",
            json_data=data,
            cast_to=None,  # type: ignore[arg-type]
        )
