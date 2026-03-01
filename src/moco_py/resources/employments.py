"""User Employments resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.employments import Employment, EmploymentPattern


class Employments(SyncResource):
    """Synchronous employments resource."""

    def list(
        self,
        *,
        from_date: str | None = None,
        to: str | None = None,
        user_id: int | None = None,
    ) -> SyncPage[Employment]:
        """Retrieve all employments."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to is not None:
            params["to"] = to
        if user_id is not None:
            params["user_id"] = user_id
        return self._get_list(
            "/users/employments", params=params or None, cast_to=Employment
        )

    def get(self, employment_id: int) -> MocoResponse[Employment]:
        """Retrieve a single employment."""
        return self._get(f"/users/employments/{employment_id}", cast_to=Employment)

    def create(
        self,
        *,
        user_id: int,
        pattern: EmploymentPattern,
        from_date: str | None = None,
        to: str | None = None,
    ) -> MocoResponse[Employment]:
        """Create an employment."""
        data: dict[str, Any] = {
            "user_id": user_id,
            "pattern": pattern.model_dump(),
        }
        if from_date is not None:
            data["from"] = from_date
        if to is not None:
            data["to"] = to
        return self._post("/users/employments", json_data=data, cast_to=Employment)

    def update(
        self,
        employment_id: int,
        *,
        pattern: EmploymentPattern | None = None,
        from_date: str | None = None,
        to: str | None = None,
    ) -> MocoResponse[Employment]:
        """Update an employment."""
        data: dict[str, Any] = {}
        if pattern is not None:
            data["pattern"] = pattern.model_dump()
        if from_date is not None:
            data["from"] = from_date
        if to is not None:
            data["to"] = to
        return self._put(
            f"/users/employments/{employment_id}",
            json_data=data,
            cast_to=Employment,
        )

    def delete(self, employment_id: int) -> MocoResponse[None]:
        """Delete an employment."""
        return self._delete(f"/users/employments/{employment_id}")


class AsyncEmployments(AsyncResource):
    """Asynchronous employments resource."""

    async def list(
        self,
        *,
        from_date: str | None = None,
        to: str | None = None,
        user_id: int | None = None,
    ) -> AsyncPage[Employment]:
        """Retrieve all employments."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to is not None:
            params["to"] = to
        if user_id is not None:
            params["user_id"] = user_id
        return await self._get_list(
            "/users/employments", params=params or None, cast_to=Employment
        )

    async def get(self, employment_id: int) -> MocoResponse[Employment]:
        """Retrieve a single employment."""
        return await self._get(
            f"/users/employments/{employment_id}", cast_to=Employment
        )

    async def create(
        self,
        *,
        user_id: int,
        pattern: EmploymentPattern,
        from_date: str | None = None,
        to: str | None = None,
    ) -> MocoResponse[Employment]:
        """Create an employment."""
        data: dict[str, Any] = {
            "user_id": user_id,
            "pattern": pattern.model_dump(),
        }
        if from_date is not None:
            data["from"] = from_date
        if to is not None:
            data["to"] = to
        return await self._post(
            "/users/employments", json_data=data, cast_to=Employment
        )

    async def update(
        self,
        employment_id: int,
        *,
        pattern: EmploymentPattern | None = None,
        from_date: str | None = None,
        to: str | None = None,
    ) -> MocoResponse[Employment]:
        """Update an employment."""
        data: dict[str, Any] = {}
        if pattern is not None:
            data["pattern"] = pattern.model_dump()
        if from_date is not None:
            data["from"] = from_date
        if to is not None:
            data["to"] = to
        return await self._put(
            f"/users/employments/{employment_id}",
            json_data=data,
            cast_to=Employment,
        )

    async def delete(self, employment_id: int) -> MocoResponse[None]:
        """Delete an employment."""
        return await self._delete(f"/users/employments/{employment_id}")
