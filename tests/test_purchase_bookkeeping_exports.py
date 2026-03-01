"""Tests for the Purchase Bookkeeping Exports resource."""

from __future__ import annotations

import datetime
import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.purchase_bookkeeping_exports import PurchaseBookkeepingExports
from moco_py.types.purchase_bookkeeping_exports import PurchaseBookkeepingExport

BASE = "https://test.mocoapp.com/api/v1"

EXPORT_JSON = {
    "id": 1101,
    "from": "2015-01-01",
    "to": "2015-12-31",
    "purchase_ids": [2197, 2189, 9771],
    "comment": "2015",
    "user": {"id": 933589840, "firstname": "Tobias", "lastname": "Miesel"},
    "status": "pending",
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
def exports(client: Moco) -> PurchaseBookkeepingExports:
    return PurchaseBookkeepingExports(client._transport)


class TestPurchaseBookkeepingExportsList:
    @respx.mock
    def test_list_exports(self, exports: PurchaseBookkeepingExports) -> None:
        respx.get(f"{BASE}/purchases/bookkeeping_exports").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([EXPORT_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = exports.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], PurchaseBookkeepingExport)
        assert page.items[0].comment == "2015"


class TestPurchaseBookkeepingExportsGet:
    @respx.mock
    def test_get_export(self, exports: PurchaseBookkeepingExports) -> None:
        respx.get(f"{BASE}/purchases/bookkeeping_exports/1101").mock(
            return_value=httpx.Response(
                200, content=json.dumps(EXPORT_JSON).encode()
            )
        )
        resp = exports.get(1101)
        assert resp.parsed.id == 1101
        assert resp.parsed.from_date == datetime.date(2015, 1, 1)
        assert resp.parsed.to_date == datetime.date(2015, 12, 31)


class TestPurchaseBookkeepingExportsCreate:
    @respx.mock
    def test_create_export(self, exports: PurchaseBookkeepingExports) -> None:
        respx.post(f"{BASE}/purchases/bookkeeping_exports").mock(
            return_value=httpx.Response(
                200, content=json.dumps(EXPORT_JSON).encode()
            )
        )
        resp = exports.create(
            purchase_ids=[2197, 2189, 9771], comment="2015"
        )
        assert resp.parsed.id == 1101
