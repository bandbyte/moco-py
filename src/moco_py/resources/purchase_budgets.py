"""Purchase Budgets resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from ..types.purchase_budgets import PurchaseBudget


class PurchaseBudgets(SyncResource):
    """Synchronous purchase budgets resource."""

    def list(self, *, year: int | None = None) -> SyncPage[PurchaseBudget]:
        """Retrieve purchase budgets for a given year."""
        params: dict[str, Any] = {}
        if year is not None:
            params["year"] = year
        return self._get_list(
            "/purchases/budgets",
            params=params,
            cast_to=PurchaseBudget,
        )


class AsyncPurchaseBudgets(AsyncResource):
    """Asynchronous purchase budgets resource."""

    async def list(self, *, year: int | None = None) -> AsyncPage[PurchaseBudget]:
        """Retrieve purchase budgets for a given year."""
        params: dict[str, Any] = {}
        if year is not None:
            params["year"] = year
        return await self._get_list(
            "/purchases/budgets",
            params=params,
            cast_to=PurchaseBudget,
        )
