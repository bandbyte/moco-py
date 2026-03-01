"""Tests for MocoResponse wrapper."""

from __future__ import annotations

import httpx

from moco_py._response import MocoResponse


class TestMocoResponse:
    def test_parsed_access(self) -> None:
        resp = httpx.Response(
            200,
            json={"id": 1},
            request=httpx.Request("GET", "https://test.mocoapp.com/api/v1/test"),
        )
        wrapped = MocoResponse(parsed={"id": 1}, http_response=resp)
        assert wrapped.parsed == {"id": 1}

    def test_status_code(self) -> None:
        resp = httpx.Response(
            201,
            json={},
            request=httpx.Request("POST", "https://test.mocoapp.com/api/v1/test"),
        )
        wrapped = MocoResponse(parsed=None, http_response=resp)
        assert wrapped.status_code == 201

    def test_headers(self) -> None:
        resp = httpx.Response(
            200,
            json={},
            headers={"X-Total": "42"},
            request=httpx.Request("GET", "https://test.mocoapp.com/api/v1/test"),
        )
        wrapped = MocoResponse(parsed=None, http_response=resp)
        assert wrapped.headers["X-Total"] == "42"

    def test_raw_response_accessible(self) -> None:
        resp = httpx.Response(
            200,
            json={},
            request=httpx.Request("GET", "https://test.mocoapp.com/api/v1/test"),
        )
        wrapped = MocoResponse(parsed="data", http_response=resp)
        assert wrapped.http_response is resp
