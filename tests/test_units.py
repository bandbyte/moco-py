"""Tests for the Units (Teams) resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.types.units import Unit

BASE = "https://test.mocoapp.com/api/v1"

UNIT_JSON = {
    "id": 1,
    "name": "Engineering",
    "users": [
        {
            "id": 10,
            "firstname": "Alice",
            "lastname": "Smith",
            "email": "alice@example.com",
        }
    ],
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


class TestUnitsList:
    @respx.mock
    def test_list_units(self, client: Moco) -> None:
        respx.get(f"{BASE}/units").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([UNIT_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = client.units.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Unit)
        assert page.items[0].name == "Engineering"
        assert page.items[0].users[0].firstname == "Alice"


class TestUnitsGet:
    @respx.mock
    def test_get_unit(self, client: Moco) -> None:
        respx.get(f"{BASE}/units/1").mock(
            return_value=httpx.Response(
                200, content=json.dumps(UNIT_JSON).encode()
            )
        )
        resp = client.units.get(1)
        assert resp.parsed.id == 1
        assert resp.parsed.name == "Engineering"


class TestUnitsCreate:
    @respx.mock
    def test_create_unit(self, client: Moco) -> None:
        respx.post(f"{BASE}/units").mock(
            return_value=httpx.Response(
                200, content=json.dumps(UNIT_JSON).encode()
            )
        )
        resp = client.units.create(name="Engineering")
        assert resp.parsed.name == "Engineering"


class TestUnitsUpdate:
    @respx.mock
    def test_update_unit(self, client: Moco) -> None:
        updated = {**UNIT_JSON, "name": "Platform"}
        respx.put(f"{BASE}/units/1").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = client.units.update(1, name="Platform")
        assert resp.parsed.name == "Platform"


class TestUnitsDelete:
    @respx.mock
    def test_delete_unit(self, client: Moco) -> None:
        respx.delete(f"{BASE}/units/1").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = client.units.delete(1)
        assert resp.parsed is None


class TestUnitsCachedProperty:
    def test_units_is_cached(self, client: Moco) -> None:
        assert client.units is client.units
