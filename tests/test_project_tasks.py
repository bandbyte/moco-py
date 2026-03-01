"""Tests for the Project Tasks resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.project_tasks import ProjectTasks
from moco_py.types.project_tasks import ProjectTask

BASE = "https://test.mocoapp.com/api/v1"

TASK_JSON = {
    "id": 760253573,
    "name": "Projektleitung",
    "billable": True,
    "active": True,
    "budget": 2900,
    "hourly_rate": 120,
    "revenue_category": {
        "id": 126,
        "name": "Projektleitung",
        "revenue_account": 30058,
        "cost_category": "PM1",
    },
    "description": "A task description",
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}

PAGINATION_HEADERS = {"X-Page": "1", "X-Per-Page": "100", "X-Total": "1"}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def resource(client: Moco) -> ProjectTasks:
    return ProjectTasks(client._transport)


class TestProjectTasksList:
    @respx.mock
    def test_list_tasks(self, resource: ProjectTasks) -> None:
        respx.get(f"{BASE}/projects/1/tasks").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([TASK_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = resource.list(1)
        assert len(page.items) == 1
        assert isinstance(page.items[0], ProjectTask)
        assert page.items[0].name == "Projektleitung"


class TestProjectTasksGet:
    @respx.mock
    def test_get_task(self, resource: ProjectTasks) -> None:
        respx.get(f"{BASE}/projects/1/tasks/760253573").mock(
            return_value=httpx.Response(
                200, content=json.dumps(TASK_JSON).encode()
            )
        )
        resp = resource.get(1, 760253573)
        assert resp.parsed.id == 760253573


class TestProjectTasksCreate:
    @respx.mock
    def test_create_task(self, resource: ProjectTasks) -> None:
        respx.post(f"{BASE}/projects/1/tasks").mock(
            return_value=httpx.Response(
                200, content=json.dumps(TASK_JSON).encode()
            )
        )
        resp = resource.create(1, name="Projektleitung", billable=True)
        assert resp.parsed.name == "Projektleitung"


class TestProjectTasksUpdate:
    @respx.mock
    def test_update_task(self, resource: ProjectTasks) -> None:
        updated = {**TASK_JSON, "budget": 5000}
        respx.put(f"{BASE}/projects/1/tasks/760253573").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = resource.update(1, 760253573, budget=5000)
        assert resp.parsed.budget == 5000


class TestProjectTasksDelete:
    @respx.mock
    def test_delete_task(self, resource: ProjectTasks) -> None:
        respx.delete(f"{BASE}/projects/1/tasks/760253573").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = resource.delete(1, 760253573)
        assert resp.parsed is None


class TestProjectTasksDestroyAll:
    @respx.mock
    def test_destroy_all_tasks(self, resource: ProjectTasks) -> None:
        respx.delete(f"{BASE}/projects/1/tasks/destroy_all").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = resource.destroy_all(1)
        assert resp.parsed is None
