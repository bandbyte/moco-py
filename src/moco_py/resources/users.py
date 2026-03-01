"""Users resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.users import PerformanceReport, User


class Users(SyncResource):
    """Synchronous users resource."""

    def list(
        self,
        *,
        include_archived: bool | None = None,
        tags: str | None = None,
        email: str | None = None,
    ) -> SyncPage[User]:
        """Retrieve all users."""
        params: dict[str, Any] = {}
        if include_archived is not None:
            params["include_archived"] = include_archived
        if tags is not None:
            params["tags"] = tags
        if email is not None:
            params["email"] = email
        return self._get_list("/users", params=params or None, cast_to=User)

    def get(self, user_id: int) -> MocoResponse[User]:
        """Retrieve a single user."""
        return self._get(f"/users/{user_id}", cast_to=User)

    def create(
        self,
        *,
        firstname: str,
        lastname: str,
        email: str,
        unit_id: int,
        password: str | None = None,
        role_id: int | None = None,
        active: bool | None = None,
        external: bool | None = None,
        language: str | None = None,
        mobile_phone: str | None = None,
        work_phone: str | None = None,
        home_address: str | None = None,
        bday: str | None = None,
        iban: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        custom_properties: dict[str, str] | None = None,
        info: str | None = None,
        welcome_email: bool | None = None,
    ) -> MocoResponse[User]:
        """Create a user."""
        data: dict[str, Any] = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "unit_id": unit_id,
        }
        for key, val in {
            "password": password,
            "role_id": role_id,
            "active": active,
            "external": external,
            "language": language,
            "mobile_phone": mobile_phone,
            "work_phone": work_phone,
            "home_address": home_address,
            "bday": bday,
            "iban": iban,
            "tags": tags,
            "custom_properties": custom_properties,
            "info": info,
            "welcome_email": welcome_email,
        }.items():
            if val is not None:
                data[key] = val
        return self._post("/users", json_data=data, cast_to=User)

    def update(
        self,
        user_id: int,
        *,
        firstname: str | None = None,
        lastname: str | None = None,
        email: str | None = None,
        unit_id: int | None = None,
        password: str | None = None,
        role_id: int | None = None,
        active: bool | None = None,
        external: bool | None = None,
        language: str | None = None,
        mobile_phone: str | None = None,
        work_phone: str | None = None,
        home_address: str | None = None,
        bday: str | None = None,
        iban: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        custom_properties: dict[str, str] | None = None,
        info: str | None = None,
    ) -> MocoResponse[User]:
        """Update a user."""
        data: dict[str, Any] = {}
        for key, val in {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "unit_id": unit_id,
            "password": password,
            "role_id": role_id,
            "active": active,
            "external": external,
            "language": language,
            "mobile_phone": mobile_phone,
            "work_phone": work_phone,
            "home_address": home_address,
            "bday": bday,
            "iban": iban,
            "tags": tags,
            "custom_properties": custom_properties,
            "info": info,
        }.items():
            if val is not None:
                data[key] = val
        return self._put(f"/users/{user_id}", json_data=data, cast_to=User)

    def delete(self, user_id: int) -> MocoResponse[None]:
        """Delete a user."""
        return self._delete(f"/users/{user_id}")

    def performance_report(
        self, user_id: int, *, year: int | None = None
    ) -> MocoResponse[PerformanceReport]:
        """Retrieve a performance report for a user."""
        params: dict[str, Any] = {}
        if year is not None:
            params["year"] = year
        return self._get(
            f"/users/{user_id}/performance_report",
            params=params or None,
            cast_to=PerformanceReport,
        )


class AsyncUsers(AsyncResource):
    """Asynchronous users resource."""

    async def list(
        self,
        *,
        include_archived: bool | None = None,
        tags: str | None = None,
        email: str | None = None,
    ) -> AsyncPage[User]:
        """Retrieve all users."""
        params: dict[str, Any] = {}
        if include_archived is not None:
            params["include_archived"] = include_archived
        if tags is not None:
            params["tags"] = tags
        if email is not None:
            params["email"] = email
        return await self._get_list("/users", params=params or None, cast_to=User)

    async def get(self, user_id: int) -> MocoResponse[User]:
        """Retrieve a single user."""
        return await self._get(f"/users/{user_id}", cast_to=User)

    async def create(
        self,
        *,
        firstname: str,
        lastname: str,
        email: str,
        unit_id: int,
        password: str | None = None,
        role_id: int | None = None,
        active: bool | None = None,
        external: bool | None = None,
        language: str | None = None,
        mobile_phone: str | None = None,
        work_phone: str | None = None,
        home_address: str | None = None,
        bday: str | None = None,
        iban: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        custom_properties: dict[str, str] | None = None,
        info: str | None = None,
        welcome_email: bool | None = None,
    ) -> MocoResponse[User]:
        """Create a user."""
        data: dict[str, Any] = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "unit_id": unit_id,
        }
        for key, val in {
            "password": password,
            "role_id": role_id,
            "active": active,
            "external": external,
            "language": language,
            "mobile_phone": mobile_phone,
            "work_phone": work_phone,
            "home_address": home_address,
            "bday": bday,
            "iban": iban,
            "tags": tags,
            "custom_properties": custom_properties,
            "info": info,
            "welcome_email": welcome_email,
        }.items():
            if val is not None:
                data[key] = val
        return await self._post("/users", json_data=data, cast_to=User)

    async def update(
        self,
        user_id: int,
        *,
        firstname: str | None = None,
        lastname: str | None = None,
        email: str | None = None,
        unit_id: int | None = None,
        password: str | None = None,
        role_id: int | None = None,
        active: bool | None = None,
        external: bool | None = None,
        language: str | None = None,
        mobile_phone: str | None = None,
        work_phone: str | None = None,
        home_address: str | None = None,
        bday: str | None = None,
        iban: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        custom_properties: dict[str, str] | None = None,
        info: str | None = None,
    ) -> MocoResponse[User]:
        """Update a user."""
        data: dict[str, Any] = {}
        for key, val in {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "unit_id": unit_id,
            "password": password,
            "role_id": role_id,
            "active": active,
            "external": external,
            "language": language,
            "mobile_phone": mobile_phone,
            "work_phone": work_phone,
            "home_address": home_address,
            "bday": bday,
            "iban": iban,
            "tags": tags,
            "custom_properties": custom_properties,
            "info": info,
        }.items():
            if val is not None:
                data[key] = val
        return await self._put(f"/users/{user_id}", json_data=data, cast_to=User)

    async def delete(self, user_id: int) -> MocoResponse[None]:
        """Delete a user."""
        return await self._delete(f"/users/{user_id}")

    async def performance_report(
        self, user_id: int, *, year: int | None = None
    ) -> MocoResponse[PerformanceReport]:
        """Retrieve a performance report for a user."""
        params: dict[str, Any] = {}
        if year is not None:
            params["year"] = year
        return await self._get(
            f"/users/{user_id}/performance_report",
            params=params or None,
            cast_to=PerformanceReport,
        )
