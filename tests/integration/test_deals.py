"""Integration tests for the Deals resource."""

from __future__ import annotations

import pytest

from moco_py import Moco
from moco_py.types.deals import Deal

pytestmark = pytest.mark.integration


class TestDealsList:
    def test_list_returns_deals(self, moco_client: Moco) -> None:
        page = moco_client.deals.list()
        assert isinstance(page.items, list)


class TestDealsMutations:
    def test_create_get_update_delete(
        self, moco_client: Moco, current_user_id: int
    ) -> None:
        # Need a deal category first
        category = moco_client.deal_categories.create(
            name="__moco_py_test__deal_cat", probability=50
        ).parsed
        try:
            created = moco_client.deals.create(
                name="__moco_py_test__deal",
                currency="EUR",
                money=1000.0,
                reminder_date="2026-12-31",
                user_id=current_user_id,
                deal_category_id=category.id,
            ).parsed
            try:
                assert isinstance(created, Deal)
                assert created.name == "__moco_py_test__deal"

                fetched = moco_client.deals.get(created.id).parsed
                assert fetched.id == created.id

                updated = moco_client.deals.update(
                    created.id, name="__moco_py_test__deal_updated"
                ).parsed
                assert updated.name == "__moco_py_test__deal_updated"
            finally:
                moco_client.deals.delete(created.id)
        finally:
            moco_client.deal_categories.delete(category.id)
