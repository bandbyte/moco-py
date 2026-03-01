"""Tests for the Account Web Hooks resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.account_web_hooks import AccountWebHooks
from moco_py.types.account_web_hooks import WebHook

BASE = "https://test.mocoapp.com/api/v1"

WEBHOOK_JSON = {
    "id": 123,
    "target": "Activity",
    "event": "create",
    "hook": "https://example.org/do-stuff",
    "disabled": False,
    "disabled_at": None,
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def web_hooks(client: Moco) -> AccountWebHooks:
    return AccountWebHooks(client._transport)


class TestWebHooksList:
    @respx.mock
    def test_list_web_hooks(self, web_hooks: AccountWebHooks) -> None:
        respx.get(f"{BASE}/account/web_hooks").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([WEBHOOK_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = web_hooks.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], WebHook)
        assert page.items[0].target == "Activity"


class TestWebHooksGet:
    @respx.mock
    def test_get_web_hook(self, web_hooks: AccountWebHooks) -> None:
        respx.get(f"{BASE}/account/web_hooks/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(WEBHOOK_JSON).encode()
            )
        )
        resp = web_hooks.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.hook == "https://example.org/do-stuff"


class TestWebHooksCreate:
    @respx.mock
    def test_create_web_hook(self, web_hooks: AccountWebHooks) -> None:
        respx.post(f"{BASE}/account/web_hooks").mock(
            return_value=httpx.Response(
                200, content=json.dumps(WEBHOOK_JSON).encode()
            )
        )
        resp = web_hooks.create(
            target="Activity", event="create", hook="https://example.org/do-stuff"
        )
        assert resp.parsed.target == "Activity"


class TestWebHooksUpdate:
    @respx.mock
    def test_update_web_hook(self, web_hooks: AccountWebHooks) -> None:
        updated = {**WEBHOOK_JSON, "hook": "https://example.org/v2"}
        respx.put(f"{BASE}/account/web_hooks/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = web_hooks.update(123, hook="https://example.org/v2")
        assert resp.parsed.hook == "https://example.org/v2"


class TestWebHooksDisable:
    @respx.mock
    def test_disable_web_hook(self, web_hooks: AccountWebHooks) -> None:
        disabled = {**WEBHOOK_JSON, "disabled": True}
        respx.put(f"{BASE}/account/web_hooks/123/disable").mock(
            return_value=httpx.Response(
                200, content=json.dumps(disabled).encode()
            )
        )
        resp = web_hooks.disable(123)
        assert resp.parsed.disabled is True


class TestWebHooksEnable:
    @respx.mock
    def test_enable_web_hook(self, web_hooks: AccountWebHooks) -> None:
        respx.put(f"{BASE}/account/web_hooks/123/enable").mock(
            return_value=httpx.Response(
                200, content=json.dumps(WEBHOOK_JSON).encode()
            )
        )
        resp = web_hooks.enable(123)
        assert resp.parsed.disabled is False


class TestWebHooksDelete:
    @respx.mock
    def test_delete_web_hook(self, web_hooks: AccountWebHooks) -> None:
        respx.delete(f"{BASE}/account/web_hooks/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = web_hooks.delete(123)
        assert resp.parsed is None
