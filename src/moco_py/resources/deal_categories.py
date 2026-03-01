"""Deal Categories resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.deal_categories import DealCategory


class DealCategories(SyncResource):
    """Synchronous deal categories resource."""

    def list(self) -> SyncPage[DealCategory]:
        """Retrieve all deal categories."""
        return self._get_list("/deal_categories", cast_to=DealCategory)

    def get(self, deal_category_id: int) -> MocoResponse[DealCategory]:
        """Retrieve a single deal category."""
        return self._get(f"/deal_categories/{deal_category_id}", cast_to=DealCategory)

    def create(
        self,
        *,
        name: str,
        probability: int,
    ) -> MocoResponse[DealCategory]:
        """Create a deal category."""
        body: dict[str, Any] = {"name": name, "probability": probability}
        return self._post("/deal_categories", json_data=body, cast_to=DealCategory)

    def update(
        self,
        deal_category_id: int,
        *,
        name: str | None = None,
        probability: int | None = None,
    ) -> MocoResponse[DealCategory]:
        """Update a deal category."""
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if probability is not None:
            body["probability"] = probability
        return self._put(
            f"/deal_categories/{deal_category_id}",
            json_data=body,
            cast_to=DealCategory,
        )

    def delete(self, deal_category_id: int) -> MocoResponse[None]:
        """Delete a deal category."""
        return self._delete(f"/deal_categories/{deal_category_id}")


class AsyncDealCategories(AsyncResource):
    """Asynchronous deal categories resource."""

    async def list(self) -> AsyncPage[DealCategory]:
        """Retrieve all deal categories."""
        return await self._get_list("/deal_categories", cast_to=DealCategory)

    async def get(self, deal_category_id: int) -> MocoResponse[DealCategory]:
        """Retrieve a single deal category."""
        return await self._get(
            f"/deal_categories/{deal_category_id}", cast_to=DealCategory
        )

    async def create(
        self,
        *,
        name: str,
        probability: int,
    ) -> MocoResponse[DealCategory]:
        """Create a deal category."""
        body: dict[str, Any] = {"name": name, "probability": probability}
        return await self._post(
            "/deal_categories", json_data=body, cast_to=DealCategory
        )

    async def update(
        self,
        deal_category_id: int,
        *,
        name: str | None = None,
        probability: int | None = None,
    ) -> MocoResponse[DealCategory]:
        """Update a deal category."""
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if probability is not None:
            body["probability"] = probability
        return await self._put(
            f"/deal_categories/{deal_category_id}",
            json_data=body,
            cast_to=DealCategory,
        )

    async def delete(self, deal_category_id: int) -> MocoResponse[None]:
        """Delete a deal category."""
        return await self._delete(f"/deal_categories/{deal_category_id}")
