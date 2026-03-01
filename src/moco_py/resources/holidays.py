"""User Holidays resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.holidays import Holiday


class Holidays(SyncResource):
    """Synchronous holidays resource."""

    def list(
        self,
        *,
        year: int | None = None,
        user_id: int | None = None,
    ) -> SyncPage[Holiday]:
        """Retrieve all holidays."""
        params: dict[str, Any] = {}
        if year is not None:
            params["year"] = year
        if user_id is not None:
            params["user_id"] = user_id
        return self._get_list("/users/holidays", params=params or None, cast_to=Holiday)

    def get(self, holiday_id: int) -> MocoResponse[Holiday]:
        """Retrieve a single holiday."""
        return self._get(f"/users/holidays/{holiday_id}", cast_to=Holiday)

    def create(
        self,
        *,
        year: int,
        title: str,
        days: int,
        user_id: int,
        creator_id: int | None = None,
    ) -> MocoResponse[Holiday]:
        """Create a holiday."""
        data: dict[str, Any] = {
            "year": year,
            "title": title,
            "days": days,
            "user_id": user_id,
        }
        if creator_id is not None:
            data["creator_id"] = creator_id
        return self._post("/users/holidays", json_data=data, cast_to=Holiday)

    def update(
        self,
        holiday_id: int,
        *,
        year: int | None = None,
        title: str | None = None,
        days: int | None = None,
        user_id: int | None = None,
        creator_id: int | None = None,
    ) -> MocoResponse[Holiday]:
        """Update a holiday."""
        data: dict[str, Any] = {}
        for key, val in {
            "year": year,
            "title": title,
            "days": days,
            "user_id": user_id,
            "creator_id": creator_id,
        }.items():
            if val is not None:
                data[key] = val
        return self._put(
            f"/users/holidays/{holiday_id}",
            json_data=data,
            cast_to=Holiday,
        )

    def delete(self, holiday_id: int) -> MocoResponse[None]:
        """Delete a holiday."""
        return self._delete(f"/users/holidays/{holiday_id}")


class AsyncHolidays(AsyncResource):
    """Asynchronous holidays resource."""

    async def list(
        self,
        *,
        year: int | None = None,
        user_id: int | None = None,
    ) -> AsyncPage[Holiday]:
        """Retrieve all holidays."""
        params: dict[str, Any] = {}
        if year is not None:
            params["year"] = year
        if user_id is not None:
            params["user_id"] = user_id
        return await self._get_list(
            "/users/holidays", params=params or None, cast_to=Holiday
        )

    async def get(self, holiday_id: int) -> MocoResponse[Holiday]:
        """Retrieve a single holiday."""
        return await self._get(f"/users/holidays/{holiday_id}", cast_to=Holiday)

    async def create(
        self,
        *,
        year: int,
        title: str,
        days: int,
        user_id: int,
        creator_id: int | None = None,
    ) -> MocoResponse[Holiday]:
        """Create a holiday."""
        data: dict[str, Any] = {
            "year": year,
            "title": title,
            "days": days,
            "user_id": user_id,
        }
        if creator_id is not None:
            data["creator_id"] = creator_id
        return await self._post("/users/holidays", json_data=data, cast_to=Holiday)

    async def update(
        self,
        holiday_id: int,
        *,
        year: int | None = None,
        title: str | None = None,
        days: int | None = None,
        user_id: int | None = None,
        creator_id: int | None = None,
    ) -> MocoResponse[Holiday]:
        """Update a holiday."""
        data: dict[str, Any] = {}
        for key, val in {
            "year": year,
            "title": title,
            "days": days,
            "user_id": user_id,
            "creator_id": creator_id,
        }.items():
            if val is not None:
                data[key] = val
        return await self._put(
            f"/users/holidays/{holiday_id}",
            json_data=data,
            cast_to=Holiday,
        )

    async def delete(self, holiday_id: int) -> MocoResponse[None]:
        """Delete a holiday."""
        return await self._delete(f"/users/holidays/{holiday_id}")
