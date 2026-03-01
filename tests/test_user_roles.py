"""Tests for the User Permission Roles resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.types.user_roles import UserRole

BASE = "https://test.mocoapp.com/api/v1"

USER_ROLE_JSON = {
    "id": 42,
    "name": "Entwickler",
    "is_default": False,
    "is_admin": False,
    "permission": {
        "report": "none",
        "companies": "full",
        "contacts": "full",
        "people": "none",
        "purchases": "none",
        "settings": "none",
        "sales": "none",
        "projects": "full",
        "calendar": "full",
        "time_tracking": "full",
        "invoicing": "none",
    },
    "created_at": "2024-10-17T09:33:46Z",
    "updated_at": "2024-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


class TestUserRolesList:
    @respx.mock
    def test_list_user_roles(self, client: Moco) -> None:
        respx.get(f"{BASE}/users/roles").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([USER_ROLE_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = client.user_roles.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], UserRole)
        assert page.items[0].name == "Entwickler"
        assert page.items[0].permission.projects == "full"
