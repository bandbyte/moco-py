"""User Presences resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.presences import Presence


class Presences(SyncResource):
    """Synchronous presences resource."""

    def list(
        self,
        *,
        from_date: str | None = None,
        to: str | None = None,
        user_id: int | None = None,
        is_home_office: bool | None = None,
    ) -> SyncPage[Presence]:
        """Retrieve all presences."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to is not None:
            params["to"] = to
        if user_id is not None:
            params["user_id"] = user_id
        if is_home_office is not None:
            params["is_home_office"] = is_home_office
        return self._get_list(
            "/users/presences", params=params or None, cast_to=Presence
        )

    def get(self, presence_id: int) -> MocoResponse[Presence]:
        """Retrieve a single presence."""
        return self._get(f"/users/presences/{presence_id}", cast_to=Presence)

    def create(
        self,
        *,
        date: str,
        from_time: str,
        to: str | None = None,
        is_home_office: bool | None = None,
    ) -> MocoResponse[Presence]:
        """Create a presence."""
        data: dict[str, Any] = {
            "date": date,
            "from": from_time,
        }
        if to is not None:
            data["to"] = to
        if is_home_office is not None:
            data["is_home_office"] = is_home_office
        return self._post("/users/presences", json_data=data, cast_to=Presence)

    def touch(
        self,
        *,
        is_home_office: bool | None = None,
        override: str | None = None,
    ) -> MocoResponse[Presence]:
        """Touch presence (clock in/out)."""
        data: dict[str, Any] = {}
        if is_home_office is not None:
            data["is_home_office"] = is_home_office
        if override is not None:
            data["override"] = override
        return self._post(
            "/users/presences/touch",
            json_data=data or None,
            cast_to=Presence,
        )

    def update(
        self,
        presence_id: int,
        *,
        date: str | None = None,
        from_time: str | None = None,
        to: str | None = None,
        is_home_office: bool | None = None,
    ) -> MocoResponse[Presence]:
        """Update a presence."""
        data: dict[str, Any] = {}
        if date is not None:
            data["date"] = date
        if from_time is not None:
            data["from"] = from_time
        if to is not None:
            data["to"] = to
        if is_home_office is not None:
            data["is_home_office"] = is_home_office
        return self._put(
            f"/users/presences/{presence_id}",
            json_data=data,
            cast_to=Presence,
        )

    def delete(self, presence_id: int) -> MocoResponse[None]:
        """Delete a presence."""
        return self._delete(f"/users/presences/{presence_id}")


class AsyncPresences(AsyncResource):
    """Asynchronous presences resource."""

    async def list(
        self,
        *,
        from_date: str | None = None,
        to: str | None = None,
        user_id: int | None = None,
        is_home_office: bool | None = None,
    ) -> AsyncPage[Presence]:
        """Retrieve all presences."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to is not None:
            params["to"] = to
        if user_id is not None:
            params["user_id"] = user_id
        if is_home_office is not None:
            params["is_home_office"] = is_home_office
        return await self._get_list(
            "/users/presences", params=params or None, cast_to=Presence
        )

    async def get(self, presence_id: int) -> MocoResponse[Presence]:
        """Retrieve a single presence."""
        return await self._get(f"/users/presences/{presence_id}", cast_to=Presence)

    async def create(
        self,
        *,
        date: str,
        from_time: str,
        to: str | None = None,
        is_home_office: bool | None = None,
    ) -> MocoResponse[Presence]:
        """Create a presence."""
        data: dict[str, Any] = {
            "date": date,
            "from": from_time,
        }
        if to is not None:
            data["to"] = to
        if is_home_office is not None:
            data["is_home_office"] = is_home_office
        return await self._post("/users/presences", json_data=data, cast_to=Presence)

    async def touch(
        self,
        *,
        is_home_office: bool | None = None,
        override: str | None = None,
    ) -> MocoResponse[Presence]:
        """Touch presence (clock in/out)."""
        data: dict[str, Any] = {}
        if is_home_office is not None:
            data["is_home_office"] = is_home_office
        if override is not None:
            data["override"] = override
        return await self._post(
            "/users/presences/touch",
            json_data=data or None,
            cast_to=Presence,
        )

    async def update(
        self,
        presence_id: int,
        *,
        date: str | None = None,
        from_time: str | None = None,
        to: str | None = None,
        is_home_office: bool | None = None,
    ) -> MocoResponse[Presence]:
        """Update a presence."""
        data: dict[str, Any] = {}
        if date is not None:
            data["date"] = date
        if from_time is not None:
            data["from"] = from_time
        if to is not None:
            data["to"] = to
        if is_home_office is not None:
            data["is_home_office"] = is_home_office
        return await self._put(
            f"/users/presences/{presence_id}",
            json_data=data,
            cast_to=Presence,
        )

    async def delete(self, presence_id: int) -> MocoResponse[None]:
        """Delete a presence."""
        return await self._delete(f"/users/presences/{presence_id}")
