"""Purchase Categories resource."""

from __future__ import annotations

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.purchase_categories import PurchaseCategory


class PurchaseCategories(SyncResource):
    """Synchronous purchase categories resource."""

    def list(self) -> SyncPage[PurchaseCategory]:
        """Retrieve all purchase categories."""
        return self._get_list("/purchases/categories", cast_to=PurchaseCategory)

    def get(self, category_id: int) -> MocoResponse[PurchaseCategory]:
        """Retrieve a single purchase category."""
        return self._get(
            f"/purchases/categories/{category_id}", cast_to=PurchaseCategory
        )


class AsyncPurchaseCategories(AsyncResource):
    """Asynchronous purchase categories resource."""

    async def list(self) -> AsyncPage[PurchaseCategory]:
        """Retrieve all purchase categories."""
        return await self._get_list("/purchases/categories", cast_to=PurchaseCategory)

    async def get(self, category_id: int) -> MocoResponse[PurchaseCategory]:
        """Retrieve a single purchase category."""
        return await self._get(
            f"/purchases/categories/{category_id}", cast_to=PurchaseCategory
        )
