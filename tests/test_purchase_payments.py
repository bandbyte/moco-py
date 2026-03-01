"""Tests for the Purchase Payments resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.purchase_payments import PurchasePayments
from moco_py.types.purchase_payments import PurchasePayment

BASE = "https://test.mocoapp.com/api/v1"

PAYMENT_JSON = {
    "id": 123,
    "date": "2022-03-01",
    "purchase": {
        "id": 12345,
        "identifier": "E2203-001",
        "title": "Purchase - Electronics",
    },
    "total": "1999.00",
    "created_at": "2022-03-01T09:33:46Z",
    "updated_at": "2022-03-01T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def purchase_payments(client: Moco) -> PurchasePayments:
    return PurchasePayments(client._transport)


class TestPurchasePaymentsList:
    @respx.mock
    def test_list_payments(self, purchase_payments: PurchasePayments) -> None:
        respx.get(f"{BASE}/purchases/payments").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([PAYMENT_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = purchase_payments.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], PurchasePayment)
        assert page.items[0].total == "1999.00"


class TestPurchasePaymentsGet:
    @respx.mock
    def test_get_payment(self, purchase_payments: PurchasePayments) -> None:
        respx.get(f"{BASE}/purchases/payments/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PAYMENT_JSON).encode()
            )
        )
        resp = purchase_payments.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.purchase.id == 12345


class TestPurchasePaymentsCreate:
    @respx.mock
    def test_create_payment(self, purchase_payments: PurchasePayments) -> None:
        respx.post(f"{BASE}/purchases/payments").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PAYMENT_JSON).encode()
            )
        )
        resp = purchase_payments.create(
            date="2022-03-01", total=1999.00, purchase_id=12345
        )
        assert resp.parsed.id == 123


class TestPurchasePaymentsUpdate:
    @respx.mock
    def test_update_payment(self, purchase_payments: PurchasePayments) -> None:
        updated = {**PAYMENT_JSON, "total": "2000.00"}
        respx.put(f"{BASE}/purchases/payments/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = purchase_payments.update(123, total=2000.00)
        assert resp.parsed.total == "2000.00"


class TestPurchasePaymentsDelete:
    @respx.mock
    def test_delete_payment(self, purchase_payments: PurchasePayments) -> None:
        respx.delete(f"{BASE}/purchases/payments/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = purchase_payments.delete(123)
        assert resp.parsed is None
