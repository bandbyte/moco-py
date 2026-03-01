"""Tests for the Invoice Bookkeeping Exports resource."""

from __future__ import annotations

import datetime
import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.invoice_bookkeeping_exports import InvoiceBookkeepingExports
from moco_py.types.invoice_bookkeeping_exports import InvoiceBookkeepingExport

BASE = "https://test.mocoapp.com/api/v1"

EXPORT_JSON = {
    "id": 1101,
    "from": "2015-01-01",
    "to": "2015-12-31",
    "invoice_ids": [2197, 2189, 9771],
    "comment": "2015",
    "user": {"id": 933589840, "firstname": "Tobias", "lastname": "Miesel"},
    "status": "manual",
    "created_at": "2021-03-23T05:38:53Z",
    "updated_at": "2021-03-23T05:38:53Z",
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
def exports(client: Moco) -> InvoiceBookkeepingExports:
    return InvoiceBookkeepingExports(client._transport)


class TestInvoiceBookkeepingExportsList:
    @respx.mock
    def test_list_exports(self, exports: InvoiceBookkeepingExports) -> None:
        respx.get(f"{BASE}/invoices/bookkeeping_exports").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([EXPORT_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = exports.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], InvoiceBookkeepingExport)
        assert page.items[0].comment == "2015"


class TestInvoiceBookkeepingExportsGet:
    @respx.mock
    def test_get_export(self, exports: InvoiceBookkeepingExports) -> None:
        respx.get(f"{BASE}/invoices/bookkeeping_exports/1101").mock(
            return_value=httpx.Response(
                200, content=json.dumps(EXPORT_JSON).encode()
            )
        )
        resp = exports.get(1101)
        assert resp.parsed.id == 1101
        assert resp.parsed.from_date == datetime.date(2015, 1, 1)
        assert resp.parsed.to_date == datetime.date(2015, 12, 31)


class TestInvoiceBookkeepingExportsCreate:
    @respx.mock
    def test_create_export(self, exports: InvoiceBookkeepingExports) -> None:
        respx.post(f"{BASE}/invoices/bookkeeping_exports").mock(
            return_value=httpx.Response(
                200, content=json.dumps(EXPORT_JSON).encode()
            )
        )
        resp = exports.create(
            invoice_ids=[2197, 2189, 9771], comment="2015"
        )
        assert resp.parsed.id == 1101
