"""Tests for exception hierarchy and _raise_for_status."""

from __future__ import annotations

import httpx
import pytest

from moco_py.exceptions import (
    AuthenticationError,
    MocoError,
    NotFoundError,
    PermissionError,
    RateLimitError,
    ServerError,
    ValidationError,
    _raise_for_status,
)


class TestMocoError:
    def test_fields(self) -> None:
        err = MocoError("fail", status_code=400, body={"x": 1})
        assert str(err) == "fail"
        assert err.message == "fail"
        assert err.status_code == 400
        assert err.body == {"x": 1}
        assert err.response is None

    def test_inheritance(self) -> None:
        assert issubclass(AuthenticationError, MocoError)
        assert issubclass(PermissionError, MocoError)
        assert issubclass(NotFoundError, MocoError)
        assert issubclass(ValidationError, MocoError)
        assert issubclass(RateLimitError, MocoError)
        assert issubclass(ServerError, MocoError)

    def test_rate_limit_retry_after(self) -> None:
        err = RateLimitError("slow down", retry_after=2.5, status_code=429)
        assert err.retry_after == 2.5


def _mock_response(
    status_code: int,
    json_body: dict | None = None,
    headers: dict[str, str] | None = None,
) -> httpx.Response:
    resp = httpx.Response(
        status_code,
        json=json_body,
        headers=headers,
        request=httpx.Request("GET", "https://test.mocoapp.com/api/v1/test"),
    )
    return resp


class TestRaiseForStatus:
    def test_200_no_raise(self) -> None:
        _raise_for_status(_mock_response(200))

    def test_401(self) -> None:
        with pytest.raises(AuthenticationError) as exc_info:
            _raise_for_status(_mock_response(401, {"message": "bad token"}))
        assert exc_info.value.status_code == 401
        assert "bad token" in str(exc_info.value)

    def test_403(self) -> None:
        with pytest.raises(PermissionError):
            _raise_for_status(_mock_response(403, {"message": "forbidden"}))

    def test_404(self) -> None:
        with pytest.raises(NotFoundError):
            _raise_for_status(_mock_response(404, {"message": "not found"}))

    def test_422(self) -> None:
        with pytest.raises(ValidationError):
            _raise_for_status(_mock_response(422, {"error": "invalid params"}))

    def test_429_with_retry_after(self) -> None:
        with pytest.raises(RateLimitError) as exc_info:
            _raise_for_status(
                _mock_response(429, {"message": "rate limited"}, {"Retry-After": "5"})
            )
        assert exc_info.value.retry_after == 5.0

    def test_429_without_retry_after(self) -> None:
        with pytest.raises(RateLimitError) as exc_info:
            _raise_for_status(_mock_response(429, {"message": "rate limited"}))
        assert exc_info.value.retry_after is None

    def test_500(self) -> None:
        with pytest.raises(ServerError) as exc_info:
            _raise_for_status(_mock_response(500))
        assert exc_info.value.status_code == 500

    def test_502(self) -> None:
        with pytest.raises(ServerError):
            _raise_for_status(_mock_response(502))

    def test_unknown_4xx(self) -> None:
        with pytest.raises(MocoError):
            _raise_for_status(_mock_response(418))

    def test_json_body_preserved(self) -> None:
        body = {"message": "oops", "details": [1, 2]}
        with pytest.raises(MocoError) as exc_info:
            _raise_for_status(_mock_response(400, body))
        assert exc_info.value.body == body
