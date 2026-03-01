"""Purchase Drafts resource."""

from __future__ import annotations

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.purchase_drafts import PurchaseDraft


class PurchaseDrafts(SyncResource):
    """Synchronous purchase drafts resource."""

    def list(self) -> SyncPage[PurchaseDraft]:
        """Retrieve all purchase drafts."""
        return self._get_list("/purchases/drafts", cast_to=PurchaseDraft)

    def get(self, draft_id: int) -> MocoResponse[PurchaseDraft]:
        """Retrieve a single purchase draft."""
        return self._get(f"/purchases/drafts/{draft_id}", cast_to=PurchaseDraft)

    def delete(self, draft_id: int) -> MocoResponse[None]:
        """Delete a purchase draft."""
        return self._delete(f"/purchases/drafts/{draft_id}")


class AsyncPurchaseDrafts(AsyncResource):
    """Asynchronous purchase drafts resource."""

    async def list(self) -> AsyncPage[PurchaseDraft]:
        """Retrieve all purchase drafts."""
        return await self._get_list("/purchases/drafts", cast_to=PurchaseDraft)

    async def get(self, draft_id: int) -> MocoResponse[PurchaseDraft]:
        """Retrieve a single purchase draft."""
        return await self._get(f"/purchases/drafts/{draft_id}", cast_to=PurchaseDraft)

    async def delete(self, draft_id: int) -> MocoResponse[None]:
        """Delete a purchase draft."""
        return await self._delete(f"/purchases/drafts/{draft_id}")
