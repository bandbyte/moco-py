"""Integration tests for the Tags resource."""

from __future__ import annotations

import pytest

from moco_py import Moco
from moco_py.types.tags import Tag

pytestmark = pytest.mark.integration


class TestTagsList:
    def test_list_returns_tags(self, moco_client: Moco) -> None:
        page = moco_client.tags.list()
        assert isinstance(page.items, list)


class TestTagsMutations:
    def test_create_update_delete(self, moco_client: Moco) -> None:
        created = moco_client.tags.create(
            name="__moco_py_test__tag",
            context="Company",
        ).parsed
        try:
            assert isinstance(created, Tag)
            assert created.name == "__moco_py_test__tag"

            updated = moco_client.tags.update(
                created.id, name="__moco_py_test__tag_updated"
            ).parsed
            assert updated.name == "__moco_py_test__tag_updated"
        finally:
            moco_client.tags.delete(created.id)
