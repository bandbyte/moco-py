"""Tests for the Project Groups resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.types.project_groups import ProjectGroup

BASE = "https://test.mocoapp.com/api/v1"

PROJECT_GROUP_JSON = {
    "id": 234,
    "name": "Project Group Name",
    "user": {
        "id": 933613686,
        "firstname": "Jane",
        "lastname": "Doe",
    },
    "company": {
        "id": 760553185,
        "name": "Acme Inc.",
    },
    "budget": 42000.0,
    "currency": "EUR",
    "info": "An info text",
    "custom_properties": {},
    "customer_report_url": "https://mycompany.mocoapp.com/project_groups/961779869/customer_report/1142853e926ee7c4dd7e",
    "projects": [
        {
            "id": 944958556,
            "identifier": "P1234",
            "name": "Project Name",
            "active": True,
            "budget": 10000.0,
        }
    ],
    "created_at": "2024-08-16T08:36:44Z",
    "updated_at": "2024-08-16T08:36:44Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


class TestProjectGroupsList:
    @respx.mock
    def test_list_project_groups(self, client: Moco) -> None:
        respx.get(f"{BASE}/projects/groups").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([PROJECT_GROUP_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = client.project_groups.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], ProjectGroup)
        assert page.items[0].name == "Project Group Name"
        assert page.items[0].projects[0].identifier == "P1234"


class TestProjectGroupsGet:
    @respx.mock
    def test_get_project_group(self, client: Moco) -> None:
        respx.get(f"{BASE}/projects/groups/234").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PROJECT_GROUP_JSON).encode()
            )
        )
        resp = client.project_groups.get(234)
        assert resp.parsed.id == 234
        assert resp.parsed.company.name == "Acme Inc."
