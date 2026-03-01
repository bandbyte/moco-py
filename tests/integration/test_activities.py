"""Integration tests for the Activities resource."""

from __future__ import annotations

import pytest

from moco_py import Moco
from moco_py.types.activities import Activity

pytestmark = pytest.mark.integration


class TestActivitiesList:
    def test_list_returns_activities(self, moco_client: Moco) -> None:
        page = moco_client.activities.list(from_date="2026-01-01", to_date="2026-12-31")
        assert isinstance(page.items, list)


class TestActivitiesMutations:
    def test_create_get_update_delete(
        self, moco_client: Moco, current_user_id: int, temp_company: int
    ) -> None:
        project = moco_client.projects.create(
            name="__moco_py_test__act_project",
            currency="EUR",
            start_date="2026-01-01",
            finish_date="2026-12-31",
            fixed_price=False,
            retainer=False,
            leader_id=current_user_id,
            customer_id=temp_company,
        ).parsed
        task = moco_client.project_tasks.create(
            project.id, name="__moco_py_test__task"
        ).parsed

        created = moco_client.activities.create(
            date="2026-06-15",
            project_id=project.id,
            task_id=task.id,
            seconds=3600,
            description="__moco_py_test__activity",
        ).parsed
        try:
            assert isinstance(created, Activity)

            fetched = moco_client.activities.get(created.id).parsed
            assert fetched.id == created.id

            updated = moco_client.activities.update(
                created.id, description="__moco_py_test__activity_updated"
            ).parsed
            assert updated.description == "__moco_py_test__activity_updated"
        finally:
            moco_client.activities.delete(created.id)
            moco_client.project_tasks.delete(project.id, task.id)
            moco_client.projects.delete(project.id)
