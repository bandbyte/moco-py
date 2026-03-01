"""Tests for base resource classes."""

from __future__ import annotations

import httpx
import respx
from pydantic import BaseModel

from moco_py._resource import SyncResource
from moco_py._transport import SyncTransport

BASE_URL = "https://test.mocoapp.com/api/v1"


class Thing(BaseModel):
    id: int
    name: str


def _make_resource() -> SyncResource:
    transport = SyncTransport(
        base_url=BASE_URL,
        api_key="test-key",
        timeout=5.0,
        max_retries=0,
    )
    return SyncResource(transport)


class TestSyncResource:
    @respx.mock
    def test_get(self) -> None:
        respx.get(f"{BASE_URL}/things/1").mock(
            return_value=httpx.Response(200, json={"id": 1, "name": "A"})
        )
        res = _make_resource()
        result = res._get("/things/1", cast_to=Thing)
        assert result.parsed.id == 1

    @respx.mock
    def test_get_list(self) -> None:
        respx.get(f"{BASE_URL}/things").mock(
            return_value=httpx.Response(
                200,
                json=[{"id": 1, "name": "A"}, {"id": 2, "name": "B"}],
                headers={"X-Page": "1", "X-Per-Page": "100", "X-Total": "2"},
            )
        )
        res = _make_resource()
        page = res._get_list("/things", cast_to=Thing)
        assert len(page.items) == 2
        assert page.page_info.total == 2

    @respx.mock
    def test_post(self) -> None:
        respx.post(f"{BASE_URL}/things").mock(
            return_value=httpx.Response(201, json={"id": 3, "name": "C"})
        )
        res = _make_resource()
        result = res._post("/things", json_data={"name": "C"}, cast_to=Thing)
        assert result.parsed.id == 3

    @respx.mock
    def test_put(self) -> None:
        respx.put(f"{BASE_URL}/things/1").mock(
            return_value=httpx.Response(200, json={"id": 1, "name": "Updated"})
        )
        res = _make_resource()
        result = res._put("/things/1", json_data={"name": "Updated"}, cast_to=Thing)
        assert result.parsed.name == "Updated"

    @respx.mock
    def test_patch(self) -> None:
        respx.patch(f"{BASE_URL}/things/1").mock(
            return_value=httpx.Response(200, json={"id": 1, "name": "Patched"})
        )
        res = _make_resource()
        result = res._patch("/things/1", json_data={"name": "Patched"}, cast_to=Thing)
        assert result.parsed.name == "Patched"

    @respx.mock
    def test_delete(self) -> None:
        respx.delete(f"{BASE_URL}/things/1").mock(
            return_value=httpx.Response(204, content=b"")
        )
        res = _make_resource()
        result = res._delete("/things/1")
        assert result.parsed is None
        assert result.status_code == 204
