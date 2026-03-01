"""Tests for the Invoice Payments resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.invoice_payments import InvoicePayments
from moco_py.types.invoice_payments import InvoicePayment

BASE = "https://test.mocoapp.com/api/v1"

PAYMENT_JSON = {
    "id": 123,
    "date": "2017-10-01",
    "invoice": {
        "id": 12345,
        "identifier": "R1710-001",
        "title": "Invoice – Website",
    },
    "paid_total": "17999.00",
    "paid_total_in_account_currency": "17999.00",
    "currency": "EUR",
    "description": "",
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}

PAGINATION_HEADERS = {
    "X-Page": "1",
    "X-Per-Page": "100",
    "X-Total": "1",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def invoice_payments(client: Moco) -> InvoicePayments:
    return InvoicePayments(client._transport)


class TestInvoicePaymentsList:
    @respx.mock
    def test_list_payments(self, invoice_payments: InvoicePayments) -> None:
        respx.get(f"{BASE}/invoices/payments").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([PAYMENT_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = invoice_payments.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], InvoicePayment)
        assert page.items[0].currency == "EUR"

    @respx.mock
    def test_list_payments_with_filters(self, invoice_payments: InvoicePayments) -> None:
        route = respx.get(f"{BASE}/invoices/payments").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        invoice_payments.list(invoice_id=123, date_from="2018-01-01")
        assert route.called


class TestInvoicePaymentsGet:
    @respx.mock
    def test_get_payment(self, invoice_payments: InvoicePayments) -> None:
        respx.get(f"{BASE}/invoices/payments/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PAYMENT_JSON).encode()
            )
        )
        resp = invoice_payments.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.invoice is not None
        assert resp.parsed.invoice.identifier == "R1710-001"


class TestInvoicePaymentsCreate:
    @respx.mock
    def test_create_payment(self, invoice_payments: InvoicePayments) -> None:
        respx.post(f"{BASE}/invoices/payments").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PAYMENT_JSON).encode()
            )
        )
        resp = invoice_payments.create(
            date="2017-10-01", paid_total=17999, invoice_id=12345
        )
        assert resp.parsed.id == 123


class TestInvoicePaymentsBulk:
    @respx.mock
    def test_create_bulk(self, invoice_payments: InvoicePayments) -> None:
        respx.post(f"{BASE}/invoices/payments/bulk").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = invoice_payments.create_bulk(
            bulk_data=[
                {"date": "2018-10-20", "invoice_id": 456, "paid_total": 2000},
                {"date": "2018-10-22", "invoice_id": 123, "paid_total": 1000},
            ]
        )
        assert resp.parsed is None


class TestInvoicePaymentsUpdate:
    @respx.mock
    def test_update_payment(self, invoice_payments: InvoicePayments) -> None:
        updated = {**PAYMENT_JSON, "paid_total": "20000.00"}
        respx.put(f"{BASE}/invoices/payments/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = invoice_payments.update(123, paid_total=20000)
        assert resp.parsed.paid_total == "20000.00"


class TestInvoicePaymentsDelete:
    @respx.mock
    def test_delete_payment(self, invoice_payments: InvoicePayments) -> None:
        respx.delete(f"{BASE}/invoices/payments/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = invoice_payments.delete(123)
        assert resp.parsed is None
