"""Tests for the VAT Codes resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.types.vat_codes import VatCodePurchase, VatCodeSale

BASE = "https://test.mocoapp.com/api/v1"

VAT_CODE_SALE_JSON = {
    "id": 186,
    "tax": 7.7,
    "reverse_charge": False,
    "intra_eu": False,
    "active": True,
    "print_gross_total": True,
    "notice_tax_exemption": "",
    "notice_tax_exemption_alt": "",
    "code": "9",
    "credit_account": "4000",
}

VAT_CODE_PURCHASE_JSON = {
    "id": 186,
    "tax": 7.7,
    "reverse_charge": False,
    "intra_eu": False,
    "active": True,
    "code": "9",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


class TestVatCodeSalesList:
    @respx.mock
    def test_list_vat_code_sales(self, client: Moco) -> None:
        respx.get(f"{BASE}/vat_code_sales").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([VAT_CODE_SALE_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = client.vat_code_sales.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], VatCodeSale)
        assert page.items[0].tax == 7.7
        assert page.items[0].code == "9"


class TestVatCodeSalesGet:
    @respx.mock
    def test_get_vat_code_sale(self, client: Moco) -> None:
        respx.get(f"{BASE}/vat_code_sales/186").mock(
            return_value=httpx.Response(
                200, content=json.dumps(VAT_CODE_SALE_JSON).encode()
            )
        )
        resp = client.vat_code_sales.get(186)
        assert resp.parsed.id == 186
        assert resp.parsed.credit_account == "4000"


class TestVatCodePurchasesList:
    @respx.mock
    def test_list_vat_code_purchases(self, client: Moco) -> None:
        respx.get(f"{BASE}/vat_code_purchases").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([VAT_CODE_PURCHASE_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = client.vat_code_purchases.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], VatCodePurchase)
        assert page.items[0].tax == 7.7


class TestVatCodePurchasesGet:
    @respx.mock
    def test_get_vat_code_purchase(self, client: Moco) -> None:
        respx.get(f"{BASE}/vat_code_purchases/186").mock(
            return_value=httpx.Response(
                200, content=json.dumps(VAT_CODE_PURCHASE_JSON).encode()
            )
        )
        resp = client.vat_code_purchases.get(186)
        assert resp.parsed.id == 186
        assert resp.parsed.code == "9"
