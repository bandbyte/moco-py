"""Tests for the Purchase Drafts resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.purchase_drafts import PurchaseDrafts
from moco_py.types.purchase_drafts import PurchaseDraft

BASE = "https://test.mocoapp.com/api/v1"

DRAFT_JSON = {
    "id": 123,
    "title": "Ticket",
    "email_from": "john@example.com",
    "email_body": "here the ticket",
    "user": {"id": 933590696, "firstname": "John", "lastname": "Doe"},
    "file_url": "https://example.com/file.pdf",
    "created_at": "2021-10-17T09:33:46Z",
    "updated_at": "2021-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def purchase_drafts(client: Moco) -> PurchaseDrafts:
    return PurchaseDrafts(client._transport)


class TestPurchaseDraftsList:
    @respx.mock
    def test_list_drafts(self, purchase_drafts: PurchaseDrafts) -> None:
        respx.get(f"{BASE}/purchases/drafts").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([DRAFT_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = purchase_drafts.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], PurchaseDraft)
        assert page.items[0].title == "Ticket"


class TestPurchaseDraftsGet:
    @respx.mock
    def test_get_draft(self, purchase_drafts: PurchaseDrafts) -> None:
        respx.get(f"{BASE}/purchases/drafts/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(DRAFT_JSON).encode()
            )
        )
        resp = purchase_drafts.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.email_from == "john@example.com"


class TestPurchaseDraftsDelete:
    @respx.mock
    def test_delete_draft(self, purchase_drafts: PurchaseDrafts) -> None:
        respx.delete(f"{BASE}/purchases/drafts/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = purchase_drafts.delete(123)
        assert resp.parsed is None
