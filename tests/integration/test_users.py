"""Integration tests for the Users resource (read-only)."""

from __future__ import annotations

import pytest

from moco_py import Moco
from moco_py.types.users import User

pytestmark = pytest.mark.integration


class TestUsersList:
    def test_list_returns_users(self, moco_client: Moco) -> None:
        page = moco_client.users.list()
        assert isinstance(page.items, list)
        assert len(page.items) >= 1  # at least the API key owner
        assert isinstance(page.items[0], User)


class TestUsersGet:
    def test_get_single_user(self, moco_client: Moco) -> None:
        page = moco_client.users.list()
        response = moco_client.users.get(page.items[0].id)
        assert isinstance(response.parsed, User)
        assert response.parsed.id == page.items[0].id
