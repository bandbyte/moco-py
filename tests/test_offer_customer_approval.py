"""Tests for the Offer Customer Approval resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.offer_customer_approval import OfferCustomerApprovals
from moco_py.types.offer_customer_approval import OfferCustomerApproval

BASE = "https://test.mocoapp.com/api/v1"

APPROVAL_JSON = {
    "id": 123,
    "approval_url": "https://example.com/offers/456/customer_approvals/abc123",
    "offer_document_url": "https://example.com/offers/456/customer_approvals/abc123/document.pdf",
    "active": False,
    "customer_full_name": None,
    "customer_email": None,
    "signature_url": None,
    "signed_at": None,
    "created_at": "2024-04-10T08:41:48Z",
    "updated_at": "2024-04-10T09:49:43Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def approvals(client: Moco) -> OfferCustomerApprovals:
    return OfferCustomerApprovals(client._transport)


class TestOfferCustomerApprovalGet:
    @respx.mock
    def test_get_approval(self, approvals: OfferCustomerApprovals) -> None:
        respx.get(f"{BASE}/offers/456/customer_approval").mock(
            return_value=httpx.Response(
                200, content=json.dumps(APPROVAL_JSON).encode()
            )
        )
        resp = approvals.get(456)
        assert resp.parsed.id == 123
        assert isinstance(resp.parsed, OfferCustomerApproval)
        assert resp.parsed.active is False


class TestOfferCustomerApprovalActivate:
    @respx.mock
    def test_activate(self, approvals: OfferCustomerApprovals) -> None:
        active_json = {**APPROVAL_JSON, "active": True}
        respx.post(f"{BASE}/offers/456/customer_approval/activate").mock(
            return_value=httpx.Response(
                200, content=json.dumps(active_json).encode()
            )
        )
        resp = approvals.activate(456)
        assert resp.parsed.active is True


class TestOfferCustomerApprovalDeactivate:
    @respx.mock
    def test_deactivate(self, approvals: OfferCustomerApprovals) -> None:
        respx.post(f"{BASE}/offers/456/customer_approval/deactivate").mock(
            return_value=httpx.Response(
                200, content=json.dumps(APPROVAL_JSON).encode()
            )
        )
        resp = approvals.deactivate(456)
        assert resp.parsed.active is False
