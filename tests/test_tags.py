"""Tests for the Tags resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.types.tags import Tag

BASE = "https://test.mocoapp.com/api/v1"

TAG_JSON = {
    "id": 12345678,
    "name": "Important",
    "color": "#FF0000",
    "context": "Project",
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


class TestTagsList:
    @respx.mock
    def test_list_tags(self, client: Moco) -> None:
        respx.get(f"{BASE}/tags").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([TAG_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = client.tags.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Tag)
        assert page.items[0].name == "Important"
        assert page.items[0].context == "Project"

    @respx.mock
    def test_list_tags_with_context(self, client: Moco) -> None:
        respx.get(f"{BASE}/tags", params={"context": "Project"}).mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([TAG_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = client.tags.list(context="Project")
        assert len(page.items) == 1


class TestTagsGet:
    @respx.mock
    def test_get_tag(self, client: Moco) -> None:
        respx.get(f"{BASE}/tags/12345678").mock(
            return_value=httpx.Response(
                200, content=json.dumps(TAG_JSON).encode()
            )
        )
        resp = client.tags.get(12345678)
        assert resp.parsed.id == 12345678
        assert resp.parsed.name == "Important"


class TestTagsCreate:
    @respx.mock
    def test_create_tag(self, client: Moco) -> None:
        respx.post(f"{BASE}/tags").mock(
            return_value=httpx.Response(
                200, content=json.dumps(TAG_JSON).encode()
            )
        )
        resp = client.tags.create(name="Important", context="Project", color="#FF0000")
        assert resp.parsed.name == "Important"
        assert resp.parsed.color == "#FF0000"


class TestTagsUpdate:
    @respx.mock
    def test_update_tag(self, client: Moco) -> None:
        updated = {**TAG_JSON, "color": "#00FF00"}
        respx.put(f"{BASE}/tags/12345678").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = client.tags.update(12345678, color="#00FF00")
        assert resp.parsed.color == "#00FF00"


class TestTagsDelete:
    @respx.mock
    def test_delete_tag(self, client: Moco) -> None:
        respx.delete(f"{BASE}/tags/12345678").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = client.tags.delete(12345678)
        assert resp.parsed is None
