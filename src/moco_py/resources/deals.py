"""Deals (Leads) resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import DealStatus
from ..types.deals import Deal


class Deals(SyncResource):
    """Synchronous deals resource."""

    def list(
        self,
        *,
        status: DealStatus | None = None,
        tags: str | None = None,
        closed_from: str | None = None,
        closed_to: str | None = None,
        company_id: int | None = None,
    ) -> SyncPage[Deal]:
        """Retrieve all deals."""
        params: dict[str, Any] = {}
        if status is not None:
            params["status"] = status
        if tags is not None:
            params["tags"] = tags
        if closed_from is not None:
            params["closed_from"] = closed_from
        if closed_to is not None:
            params["closed_to"] = closed_to
        if company_id is not None:
            params["company_id"] = company_id
        return self._get_list("/deals", params=params or None, cast_to=Deal)

    def get(self, deal_id: int) -> MocoResponse[Deal]:
        """Retrieve a single deal."""
        return self._get(f"/deals/{deal_id}", cast_to=Deal)

    def create(
        self,
        *,
        name: str,
        currency: str,
        money: float,
        reminder_date: str,
        user_id: int,
        deal_category_id: int,
        company_id: int | None = None,
        person_id: int | None = None,
        info: str | None = None,
        status: DealStatus | None = None,
        closed_on: str | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Deal]:
        """Create a deal."""
        data: dict[str, Any] = {
            "name": name,
            "currency": currency,
            "money": money,
            "reminder_date": reminder_date,
            "user_id": user_id,
            "deal_category_id": deal_category_id,
        }
        if company_id is not None:
            data["company_id"] = company_id
        if person_id is not None:
            data["person_id"] = person_id
        if info is not None:
            data["info"] = info
        if status is not None:
            data["status"] = status
        if closed_on is not None:
            data["closed_on"] = closed_on
        if service_period_from is not None:
            data["service_period_from"] = service_period_from
        if service_period_to is not None:
            data["service_period_to"] = service_period_to
        if tags is not None:
            data["tags"] = tags
        return self._post("/deals", json_data=data, cast_to=Deal)

    def update(
        self,
        deal_id: int,
        *,
        name: str | None = None,
        currency: str | None = None,
        money: float | None = None,
        reminder_date: str | None = None,
        user_id: int | None = None,
        deal_category_id: int | None = None,
        company_id: int | None = None,
        person_id: int | None = None,
        info: str | None = None,
        status: DealStatus | None = None,
        closed_on: str | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Deal]:
        """Update a deal."""
        data: dict[str, Any] = {}
        if name is not None:
            data["name"] = name
        if currency is not None:
            data["currency"] = currency
        if money is not None:
            data["money"] = money
        if reminder_date is not None:
            data["reminder_date"] = reminder_date
        if user_id is not None:
            data["user_id"] = user_id
        if deal_category_id is not None:
            data["deal_category_id"] = deal_category_id
        if company_id is not None:
            data["company_id"] = company_id
        if person_id is not None:
            data["person_id"] = person_id
        if info is not None:
            data["info"] = info
        if status is not None:
            data["status"] = status
        if closed_on is not None:
            data["closed_on"] = closed_on
        if service_period_from is not None:
            data["service_period_from"] = service_period_from
        if service_period_to is not None:
            data["service_period_to"] = service_period_to
        if tags is not None:
            data["tags"] = tags
        return self._put(f"/deals/{deal_id}", json_data=data, cast_to=Deal)

    def delete(self, deal_id: int) -> MocoResponse[None]:
        """Delete a deal."""
        return self._delete(f"/deals/{deal_id}")


class AsyncDeals(AsyncResource):
    """Asynchronous deals resource."""

    async def list(
        self,
        *,
        status: DealStatus | None = None,
        tags: str | None = None,
        closed_from: str | None = None,
        closed_to: str | None = None,
        company_id: int | None = None,
    ) -> AsyncPage[Deal]:
        """Retrieve all deals."""
        params: dict[str, Any] = {}
        if status is not None:
            params["status"] = status
        if tags is not None:
            params["tags"] = tags
        if closed_from is not None:
            params["closed_from"] = closed_from
        if closed_to is not None:
            params["closed_to"] = closed_to
        if company_id is not None:
            params["company_id"] = company_id
        return await self._get_list("/deals", params=params or None, cast_to=Deal)

    async def get(self, deal_id: int) -> MocoResponse[Deal]:
        """Retrieve a single deal."""
        return await self._get(f"/deals/{deal_id}", cast_to=Deal)

    async def create(
        self,
        *,
        name: str,
        currency: str,
        money: float,
        reminder_date: str,
        user_id: int,
        deal_category_id: int,
        company_id: int | None = None,
        person_id: int | None = None,
        info: str | None = None,
        status: DealStatus | None = None,
        closed_on: str | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Deal]:
        """Create a deal."""
        data: dict[str, Any] = {
            "name": name,
            "currency": currency,
            "money": money,
            "reminder_date": reminder_date,
            "user_id": user_id,
            "deal_category_id": deal_category_id,
        }
        if company_id is not None:
            data["company_id"] = company_id
        if person_id is not None:
            data["person_id"] = person_id
        if info is not None:
            data["info"] = info
        if status is not None:
            data["status"] = status
        if closed_on is not None:
            data["closed_on"] = closed_on
        if service_period_from is not None:
            data["service_period_from"] = service_period_from
        if service_period_to is not None:
            data["service_period_to"] = service_period_to
        if tags is not None:
            data["tags"] = tags
        return await self._post("/deals", json_data=data, cast_to=Deal)

    async def update(
        self,
        deal_id: int,
        *,
        name: str | None = None,
        currency: str | None = None,
        money: float | None = None,
        reminder_date: str | None = None,
        user_id: int | None = None,
        deal_category_id: int | None = None,
        company_id: int | None = None,
        person_id: int | None = None,
        info: str | None = None,
        status: DealStatus | None = None,
        closed_on: str | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Deal]:
        """Update a deal."""
        data: dict[str, Any] = {}
        if name is not None:
            data["name"] = name
        if currency is not None:
            data["currency"] = currency
        if money is not None:
            data["money"] = money
        if reminder_date is not None:
            data["reminder_date"] = reminder_date
        if user_id is not None:
            data["user_id"] = user_id
        if deal_category_id is not None:
            data["deal_category_id"] = deal_category_id
        if company_id is not None:
            data["company_id"] = company_id
        if person_id is not None:
            data["person_id"] = person_id
        if info is not None:
            data["info"] = info
        if status is not None:
            data["status"] = status
        if closed_on is not None:
            data["closed_on"] = closed_on
        if service_period_from is not None:
            data["service_period_from"] = service_period_from
        if service_period_to is not None:
            data["service_period_to"] = service_period_to
        if tags is not None:
            data["tags"] = tags
        return await self._put(f"/deals/{deal_id}", json_data=data, cast_to=Deal)

    async def delete(self, deal_id: int) -> MocoResponse[None]:
        """Delete a deal."""
        return await self._delete(f"/deals/{deal_id}")
