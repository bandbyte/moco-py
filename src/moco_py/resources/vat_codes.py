"""VAT Codes resource."""

from __future__ import annotations

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.vat_codes import VatCodePurchase, VatCodeSale


class VatCodeSales(SyncResource):
    """Synchronous sale VAT codes resource."""

    def list(self) -> SyncPage[VatCodeSale]:
        """Retrieve all sale VAT codes."""
        return self._get_list("/vat_code_sales", cast_to=VatCodeSale)

    def get(self, vat_code_sale_id: int) -> MocoResponse[VatCodeSale]:
        """Retrieve a single sale VAT code."""
        return self._get(f"/vat_code_sales/{vat_code_sale_id}", cast_to=VatCodeSale)


class AsyncVatCodeSales(AsyncResource):
    """Asynchronous sale VAT codes resource."""

    async def list(self) -> AsyncPage[VatCodeSale]:
        """Retrieve all sale VAT codes."""
        return await self._get_list("/vat_code_sales", cast_to=VatCodeSale)

    async def get(self, vat_code_sale_id: int) -> MocoResponse[VatCodeSale]:
        """Retrieve a single sale VAT code."""
        return await self._get(
            f"/vat_code_sales/{vat_code_sale_id}", cast_to=VatCodeSale
        )


class VatCodePurchases(SyncResource):
    """Synchronous purchase VAT codes resource."""

    def list(self) -> SyncPage[VatCodePurchase]:
        """Retrieve all purchase VAT codes."""
        return self._get_list("/vat_code_purchases", cast_to=VatCodePurchase)

    def get(self, vat_code_purchase_id: int) -> MocoResponse[VatCodePurchase]:
        """Retrieve a single purchase VAT code."""
        return self._get(
            f"/vat_code_purchases/{vat_code_purchase_id}", cast_to=VatCodePurchase
        )


class AsyncVatCodePurchases(AsyncResource):
    """Asynchronous purchase VAT codes resource."""

    async def list(self) -> AsyncPage[VatCodePurchase]:
        """Retrieve all purchase VAT codes."""
        return await self._get_list("/vat_code_purchases", cast_to=VatCodePurchase)

    async def get(self, vat_code_purchase_id: int) -> MocoResponse[VatCodePurchase]:
        """Retrieve a single purchase VAT code."""
        return await self._get(
            f"/vat_code_purchases/{vat_code_purchase_id}", cast_to=VatCodePurchase
        )
