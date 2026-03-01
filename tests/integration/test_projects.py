"""Integration tests for the Projects resource."""

from __future__ import annotations

import pytest

from moco_py import Moco
from moco_py.types.projects import Project

pytestmark = pytest.mark.integration


class TestProjectsList:
    def test_list_returns_projects(self, moco_client: Moco) -> None:
        page = moco_client.projects.list()
        assert isinstance(page.items, list)
        if page.items:
            assert isinstance(page.items[0], Project)

    def test_list_pagination_headers(self, moco_client: Moco) -> None:
        page = moco_client.projects.list()
        info = page.page_info
        assert info.page >= 1
        assert info.per_page >= 1
        assert info.total >= 0


class TestProjectsGet:
    def test_get_single_project(self, moco_client: Moco) -> None:
        page = moco_client.projects.list()
        if not page.items:
            pytest.skip("No projects in test environment")
        response = moco_client.projects.get(page.items[0].id)
        assert isinstance(response.parsed, Project)
        assert response.parsed.id == page.items[0].id


class TestProjectsMutations:
    def test_create_get_update_delete(
        self, moco_client: Moco, current_user_id: int, temp_company: int
    ) -> None:
        created = moco_client.projects.create(
            name="__moco_py_test__project",
            currency="EUR",
            start_date="2026-01-01",
            finish_date="2026-12-31",
            fixed_price=False,
            retainer=False,
            leader_id=current_user_id,
            customer_id=temp_company,
        ).parsed
        try:
            assert isinstance(created, Project)
            assert created.name == "__moco_py_test__project"

            fetched = moco_client.projects.get(created.id).parsed
            assert fetched.id == created.id

            updated = moco_client.projects.update(
                created.id, name="__moco_py_test__project_updated"
            ).parsed
            assert updated.name == "__moco_py_test__project_updated"
        finally:
            moco_client.projects.delete(created.id)
