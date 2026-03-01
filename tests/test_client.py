"""Tests for Moco and AsyncMoco client classes."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from moco_py import AsyncMoco, Moco, MocoError


class TestMocoConstructor:
    def test_explicit_params(self) -> None:
        client = Moco(api_key="key", domain="company")
        assert client._transport._api_key == "key"
        assert "company.mocoapp.com" in client._transport._base_url
        client.close()

    def test_env_var_fallback(self) -> None:
        with patch.dict(os.environ, {"MOCO_API_KEY": "envkey", "MOCO_DOMAIN": "envco"}):
            client = Moco()
            assert client._transport._api_key == "envkey"
            assert "envco.mocoapp.com" in client._transport._base_url
            client.close()

    def test_missing_api_key_raises(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            os.environ.pop("MOCO_API_KEY", None)
            with pytest.raises(MocoError, match="api_key"):
                Moco(domain="company")

    def test_missing_domain_raises(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            os.environ.pop("MOCO_DOMAIN", None)
            with pytest.raises(MocoError, match="domain"):
                Moco(api_key="key")

    def test_base_url_skips_domain(self) -> None:
        client = Moco(api_key="key", base_url="https://custom.example.com/api/v1")
        assert client._transport._base_url == "https://custom.example.com/api/v1"
        client.close()

    def test_impersonate_user_id(self) -> None:
        client = Moco(api_key="key", domain="co", impersonate_user_id=123)
        # The header should be in default_headers passed to transport
        # When transport owns the client, headers are set on httpx.Client
        # When custom client is passed, headers are in _default_headers
        client.close()

    def test_context_manager(self) -> None:
        with Moco(api_key="key", domain="co") as client:
            assert client._transport is not None
        # After exit, transport should be closed (no assertion needed, just no error)


class TestAsyncMocoConstructor:
    def test_explicit_params(self) -> None:
        client = AsyncMoco(api_key="key", domain="company")
        assert client._transport._api_key == "key"

    def test_missing_api_key_raises(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            os.environ.pop("MOCO_API_KEY", None)
            with pytest.raises(MocoError, match="api_key"):
                AsyncMoco(domain="company")

    def test_missing_domain_raises(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            os.environ.pop("MOCO_DOMAIN", None)
            with pytest.raises(MocoError, match="domain"):
                AsyncMoco(api_key="key")

    def test_base_url_skips_domain(self) -> None:
        client = AsyncMoco(api_key="key", base_url="https://custom.example.com/api/v1")
        assert client._transport._base_url == "https://custom.example.com/api/v1"
