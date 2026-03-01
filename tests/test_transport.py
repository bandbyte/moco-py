"""Tests for SyncTransport."""

from __future__ import annotations

from unittest.mock import patch

import httpx
import pytest
import respx
from pydantic import BaseModel

from moco_py._transport import SyncTransport
from moco_py.exceptions import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)

BASE_URL = "https://test.mocoapp.com/api/v1"


class DummyModel(BaseModel):
    id: int
    name: str


def _make_transport(max_retries: int = 0) -> SyncTransport:
    return SyncTransport(
        base_url=BASE_URL,
        api_key="test-key",
        timeout=5.0,
        max_retries=max_retries,
    )


class TestSyncTransportRequest:
    @respx.mock
    def test_get_single(self) -> None:
        respx.get(f"{BASE_URL}/things/1").mock(
            return_value=httpx.Response(200, json={"id": 1, "name": "Widget"})
        )
        transport = _make_transport()
        result = transport.request("GET", "/things/1", cast_to=DummyModel)
        assert result.parsed.id == 1
        assert result.parsed.name == "Widget"
        assert result.status_code == 200

    @respx.mock
    def test_get_list(self) -> None:
        respx.get(f"{BASE_URL}/things").mock(
            return_value=httpx.Response(
                200,
                json=[{"id": 1, "name": "A"}, {"id": 2, "name": "B"}],
            )
        )
        transport = _make_transport()
        result = transport.request("GET", "/things", cast_to=DummyModel, is_list=True)
        assert len(result.parsed) == 2
        assert result.parsed[0].name == "A"

    @respx.mock
    def test_post(self) -> None:
        respx.post(f"{BASE_URL}/things").mock(
            return_value=httpx.Response(201, json={"id": 3, "name": "New"})
        )
        transport = _make_transport()
        result = transport.request(
            "POST", "/things", json_data={"name": "New"}, cast_to=DummyModel
        )
        assert result.parsed.id == 3
        assert result.status_code == 201

    @respx.mock
    def test_delete_no_cast(self) -> None:
        respx.delete(f"{BASE_URL}/things/1").mock(
            return_value=httpx.Response(204, content=b"")
        )
        transport = _make_transport()
        result = transport.request("DELETE", "/things/1", cast_to=None)
        assert result.parsed is None
        assert result.status_code == 204


class TestSyncTransportErrors:
    @respx.mock
    def test_401(self) -> None:
        respx.get(f"{BASE_URL}/x").mock(
            return_value=httpx.Response(401, json={"message": "unauthorized"})
        )
        with pytest.raises(AuthenticationError):
            _make_transport().request("GET", "/x", cast_to=DummyModel)

    @respx.mock
    def test_404(self) -> None:
        respx.get(f"{BASE_URL}/x").mock(
            return_value=httpx.Response(404, json={"message": "not found"})
        )
        with pytest.raises(NotFoundError):
            _make_transport().request("GET", "/x", cast_to=DummyModel)

    @respx.mock
    def test_422(self) -> None:
        respx.get(f"{BASE_URL}/x").mock(
            return_value=httpx.Response(422, json={"message": "invalid"})
        )
        with pytest.raises(ValidationError):
            _make_transport().request("GET", "/x", cast_to=DummyModel)

    @respx.mock
    def test_500(self) -> None:
        respx.get(f"{BASE_URL}/x").mock(
            return_value=httpx.Response(500, json={"message": "server error"})
        )
        with pytest.raises(ServerError):
            _make_transport().request("GET", "/x", cast_to=DummyModel)


class TestSyncTransportRetries:
    @respx.mock
    @patch("moco_py._transport.time.sleep")
    def test_retry_on_429_with_retry_after(self, mock_sleep: object) -> None:
        route = respx.get(f"{BASE_URL}/x")
        route.side_effect = [
            httpx.Response(429, json={"message": "slow"}, headers={"Retry-After": "2"}),
            httpx.Response(200, json={"id": 1, "name": "ok"}),
        ]
        transport = _make_transport(max_retries=1)
        result = transport.request("GET", "/x", cast_to=DummyModel)
        assert result.parsed.id == 1

    @respx.mock
    @patch("moco_py._transport.time.sleep")
    def test_retry_on_500(self, mock_sleep: object) -> None:
        route = respx.get(f"{BASE_URL}/x")
        route.side_effect = [
            httpx.Response(500, json={"message": "err"}),
            httpx.Response(200, json={"id": 1, "name": "ok"}),
        ]
        transport = _make_transport(max_retries=1)
        result = transport.request("GET", "/x", cast_to=DummyModel)
        assert result.parsed.id == 1

    @respx.mock
    def test_exhausted_retries_raises(self) -> None:
        respx.get(f"{BASE_URL}/x").mock(
            return_value=httpx.Response(500, json={"message": "err"})
        )
        with pytest.raises(ServerError):
            _make_transport(max_retries=0).request("GET", "/x", cast_to=DummyModel)

    @respx.mock
    def test_429_no_retry_raises(self) -> None:
        respx.get(f"{BASE_URL}/x").mock(
            return_value=httpx.Response(429, json={"message": "slow"})
        )
        with pytest.raises(RateLimitError):
            _make_transport(max_retries=0).request("GET", "/x", cast_to=DummyModel)


class TestSyncTransportConnectionErrors:
    @respx.mock
    def test_timeout(self) -> None:
        respx.get(f"{BASE_URL}/x").mock(side_effect=httpx.ReadTimeout("timeout"))
        with pytest.raises(APITimeoutError):
            _make_transport().request("GET", "/x", cast_to=DummyModel)

    @respx.mock
    def test_connection_error(self) -> None:
        respx.get(f"{BASE_URL}/x").mock(side_effect=httpx.ConnectError("refused"))
        with pytest.raises(APIConnectionError):
            _make_transport().request("GET", "/x", cast_to=DummyModel)


class TestSyncTransportAuth:
    @respx.mock
    def test_auth_header_sent(self) -> None:
        route = respx.get(f"{BASE_URL}/x").mock(
            return_value=httpx.Response(200, json={"id": 1, "name": "ok"})
        )
        _make_transport().request("GET", "/x", cast_to=DummyModel)
        assert route.calls[0].request.headers["Authorization"] == "Token token=test-key"

    @respx.mock
    def test_custom_http_client(self) -> None:
        custom = httpx.Client(timeout=10.0)
        respx.get(f"{BASE_URL}/x").mock(
            return_value=httpx.Response(200, json={"id": 1, "name": "ok"})
        )
        transport = SyncTransport(
            base_url=BASE_URL,
            api_key="key",
            timeout=5.0,
            max_retries=0,
            http_client=custom,
        )
        result = transport.request("GET", "/x", cast_to=DummyModel)
        assert result.parsed.id == 1
        custom.close()
