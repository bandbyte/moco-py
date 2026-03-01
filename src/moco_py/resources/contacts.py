"""Contacts (People) resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import Gender
from ..types.contacts import Contact


class Contacts(SyncResource):
    """Synchronous contacts resource."""

    def list(
        self,
        *,
        tags: str | None = None,
        term: str | None = None,
        phone: str | None = None,
    ) -> SyncPage[Contact]:
        """Retrieve all contacts."""
        params: dict[str, Any] = {}
        if tags is not None:
            params["tags"] = tags
        if term is not None:
            params["term"] = term
        if phone is not None:
            params["phone"] = phone
        return self._get_list(
            "/contacts/people", params=params or None, cast_to=Contact
        )

    def get(self, contact_id: int) -> MocoResponse[Contact]:
        """Retrieve a single contact."""
        return self._get(f"/contacts/people/{contact_id}", cast_to=Contact)

    def create(
        self,
        *,
        lastname: str,
        gender: Gender,
        firstname: str | None = None,
        company_id: int | None = None,
        user_id: int | None = None,
        title: str | None = None,
        job_position: str | None = None,
        mobile_phone: str | None = None,
        work_fax: str | None = None,
        work_phone: str | None = None,
        work_email: str | None = None,
        work_address: str | None = None,
        home_email: str | None = None,
        home_address: str | None = None,
        birthday: str | None = None,
        info: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Contact]:
        """Create a contact."""
        data: dict[str, Any] = {"lastname": lastname, "gender": gender}
        if firstname is not None:
            data["firstname"] = firstname
        if company_id is not None:
            data["company_id"] = company_id
        if user_id is not None:
            data["user_id"] = user_id
        if title is not None:
            data["title"] = title
        if job_position is not None:
            data["job_position"] = job_position
        if mobile_phone is not None:
            data["mobile_phone"] = mobile_phone
        if work_fax is not None:
            data["work_fax"] = work_fax
        if work_phone is not None:
            data["work_phone"] = work_phone
        if work_email is not None:
            data["work_email"] = work_email
        if work_address is not None:
            data["work_address"] = work_address
        if home_email is not None:
            data["home_email"] = home_email
        if home_address is not None:
            data["home_address"] = home_address
        if birthday is not None:
            data["birthday"] = birthday
        if info is not None:
            data["info"] = info
        if tags is not None:
            data["tags"] = tags
        return self._post("/contacts/people", json_data=data, cast_to=Contact)

    def update(
        self,
        contact_id: int,
        *,
        firstname: str | None = None,
        lastname: str | None = None,
        gender: Gender | None = None,
        company_id: int | None = None,
        user_id: int | None = None,
        title: str | None = None,
        job_position: str | None = None,
        mobile_phone: str | None = None,
        work_fax: str | None = None,
        work_phone: str | None = None,
        work_email: str | None = None,
        work_address: str | None = None,
        home_email: str | None = None,
        home_address: str | None = None,
        birthday: str | None = None,
        info: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Contact]:
        """Update a contact."""
        data: dict[str, Any] = {}
        if firstname is not None:
            data["firstname"] = firstname
        if lastname is not None:
            data["lastname"] = lastname
        if gender is not None:
            data["gender"] = gender
        if company_id is not None:
            data["company_id"] = company_id
        if user_id is not None:
            data["user_id"] = user_id
        if title is not None:
            data["title"] = title
        if job_position is not None:
            data["job_position"] = job_position
        if mobile_phone is not None:
            data["mobile_phone"] = mobile_phone
        if work_fax is not None:
            data["work_fax"] = work_fax
        if work_phone is not None:
            data["work_phone"] = work_phone
        if work_email is not None:
            data["work_email"] = work_email
        if work_address is not None:
            data["work_address"] = work_address
        if home_email is not None:
            data["home_email"] = home_email
        if home_address is not None:
            data["home_address"] = home_address
        if birthday is not None:
            data["birthday"] = birthday
        if info is not None:
            data["info"] = info
        if tags is not None:
            data["tags"] = tags
        return self._put(
            f"/contacts/people/{contact_id}", json_data=data, cast_to=Contact
        )

    def delete(self, contact_id: int) -> MocoResponse[None]:
        """Delete a contact."""
        return self._delete(f"/contacts/people/{contact_id}")


class AsyncContacts(AsyncResource):
    """Asynchronous contacts resource."""

    async def list(
        self,
        *,
        tags: str | None = None,
        term: str | None = None,
        phone: str | None = None,
    ) -> AsyncPage[Contact]:
        """Retrieve all contacts."""
        params: dict[str, Any] = {}
        if tags is not None:
            params["tags"] = tags
        if term is not None:
            params["term"] = term
        if phone is not None:
            params["phone"] = phone
        return await self._get_list(
            "/contacts/people", params=params or None, cast_to=Contact
        )

    async def get(self, contact_id: int) -> MocoResponse[Contact]:
        """Retrieve a single contact."""
        return await self._get(f"/contacts/people/{contact_id}", cast_to=Contact)

    async def create(
        self,
        *,
        lastname: str,
        gender: Gender,
        firstname: str | None = None,
        company_id: int | None = None,
        user_id: int | None = None,
        title: str | None = None,
        job_position: str | None = None,
        mobile_phone: str | None = None,
        work_fax: str | None = None,
        work_phone: str | None = None,
        work_email: str | None = None,
        work_address: str | None = None,
        home_email: str | None = None,
        home_address: str | None = None,
        birthday: str | None = None,
        info: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Contact]:
        """Create a contact."""
        data: dict[str, Any] = {"lastname": lastname, "gender": gender}
        if firstname is not None:
            data["firstname"] = firstname
        if company_id is not None:
            data["company_id"] = company_id
        if user_id is not None:
            data["user_id"] = user_id
        if title is not None:
            data["title"] = title
        if job_position is not None:
            data["job_position"] = job_position
        if mobile_phone is not None:
            data["mobile_phone"] = mobile_phone
        if work_fax is not None:
            data["work_fax"] = work_fax
        if work_phone is not None:
            data["work_phone"] = work_phone
        if work_email is not None:
            data["work_email"] = work_email
        if work_address is not None:
            data["work_address"] = work_address
        if home_email is not None:
            data["home_email"] = home_email
        if home_address is not None:
            data["home_address"] = home_address
        if birthday is not None:
            data["birthday"] = birthday
        if info is not None:
            data["info"] = info
        if tags is not None:
            data["tags"] = tags
        return await self._post("/contacts/people", json_data=data, cast_to=Contact)

    async def update(
        self,
        contact_id: int,
        *,
        firstname: str | None = None,
        lastname: str | None = None,
        gender: Gender | None = None,
        company_id: int | None = None,
        user_id: int | None = None,
        title: str | None = None,
        job_position: str | None = None,
        mobile_phone: str | None = None,
        work_fax: str | None = None,
        work_phone: str | None = None,
        work_email: str | None = None,
        work_address: str | None = None,
        home_email: str | None = None,
        home_address: str | None = None,
        birthday: str | None = None,
        info: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Contact]:
        """Update a contact."""
        data: dict[str, Any] = {}
        if firstname is not None:
            data["firstname"] = firstname
        if lastname is not None:
            data["lastname"] = lastname
        if gender is not None:
            data["gender"] = gender
        if company_id is not None:
            data["company_id"] = company_id
        if user_id is not None:
            data["user_id"] = user_id
        if title is not None:
            data["title"] = title
        if job_position is not None:
            data["job_position"] = job_position
        if mobile_phone is not None:
            data["mobile_phone"] = mobile_phone
        if work_fax is not None:
            data["work_fax"] = work_fax
        if work_phone is not None:
            data["work_phone"] = work_phone
        if work_email is not None:
            data["work_email"] = work_email
        if work_address is not None:
            data["work_address"] = work_address
        if home_email is not None:
            data["home_email"] = home_email
        if home_address is not None:
            data["home_address"] = home_address
        if birthday is not None:
            data["birthday"] = birthday
        if info is not None:
            data["info"] = info
        if tags is not None:
            data["tags"] = tags
        return await self._put(
            f"/contacts/people/{contact_id}", json_data=data, cast_to=Contact
        )

    async def delete(self, contact_id: int) -> MocoResponse[None]:
        """Delete a contact."""
        return await self._delete(f"/contacts/people/{contact_id}")
