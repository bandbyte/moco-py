"""Tests for the Project Contracts resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.project_contracts import ProjectContracts
from moco_py.types.project_contracts import ProjectContract

BASE = "https://test.mocoapp.com/api/v1"

CONTRACT_JSON = {
    "id": 760253573,
    "user_id": 938487474,
    "firstname": "Nicola",
    "lastname": "Piccinini",
    "billable": True,
    "active": True,
    "budget": 9900,
    "hourly_rate": 110,
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}

PAGINATION_HEADERS = {"X-Page": "1", "X-Per-Page": "100", "X-Total": "1"}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def resource(client: Moco) -> ProjectContracts:
    return ProjectContracts(client._transport)


class TestProjectContractsList:
    @respx.mock
    def test_list_contracts(self, resource: ProjectContracts) -> None:
        respx.get(f"{BASE}/projects/1/contracts").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([CONTRACT_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = resource.list(1)
        assert len(page.items) == 1
        assert isinstance(page.items[0], ProjectContract)
        assert page.items[0].firstname == "Nicola"


class TestProjectContractsGet:
    @respx.mock
    def test_get_contract(self, resource: ProjectContracts) -> None:
        respx.get(f"{BASE}/projects/1/contracts/760253573").mock(
            return_value=httpx.Response(
                200, content=json.dumps(CONTRACT_JSON).encode()
            )
        )
        resp = resource.get(1, 760253573)
        assert resp.parsed.id == 760253573


class TestProjectContractsCreate:
    @respx.mock
    def test_create_contract(self, resource: ProjectContracts) -> None:
        respx.post(f"{BASE}/projects/1/contracts").mock(
            return_value=httpx.Response(
                200, content=json.dumps(CONTRACT_JSON).encode()
            )
        )
        resp = resource.create(1, user_id=938487474, budget=9900)
        assert resp.parsed.user_id == 938487474


class TestProjectContractsUpdate:
    @respx.mock
    def test_update_contract(self, resource: ProjectContracts) -> None:
        updated = {**CONTRACT_JSON, "budget": 8800}
        respx.put(f"{BASE}/projects/1/contracts/760253573").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = resource.update(1, 760253573, budget=8800)
        assert resp.parsed.budget == 8800


class TestProjectContractsDelete:
    @respx.mock
    def test_delete_contract(self, resource: ProjectContracts) -> None:
        respx.delete(f"{BASE}/projects/1/contracts/760253573").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = resource.delete(1, 760253573)
        assert resp.parsed is None
