"""Tests for the Projects resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.projects import Projects
from moco_py.types.projects import (
    AssignedProject,
    Project,
    ProjectReport,
    ProjectShareResponse,
)

BASE = "https://test.mocoapp.com/api/v1"

PROJECT_JSON = {
    "id": 1234567,
    "identifier": "P001",
    "name": "Website Support",
    "active": True,
    "billable": True,
    "fixed_price": True,
    "retainer": False,
    "start_date": None,
    "finish_date": "2018-12-31",
    "color": "#CCCC00",
    "currency": "EUR",
    "billing_variant": "project",
    "billing_address": "Beispiel AG",
    "billing_email_to": "project@beispiel.co",
    "billing_email_cc": "project-cc@beispiel.co",
    "billing_notes": "Billing notes text",
    "setting_include_time_report": True,
    "budget": 18200,
    "budget_monthly": None,
    "budget_expenses": 8200,
    "hourly_rate": 150,
    "info": "Abrechnung jaehrlich",
    "tags": ["Print", "Digital"],
    "custom_properties": {"Project Management": "https://basecamp.com/123456"},
    "leader": {"id": 933590696, "firstname": "Michael", "lastname": "Mustermann"},
    "co_leader": None,
    "customer": {"id": 1233434, "name": "Beispiel AG"},
    "deal": {"id": 5635453, "name": "Website Relaunch"},
    "tasks": [
        {
            "id": 125112,
            "name": "Project Management",
            "billable": True,
            "active": True,
            "budget": None,
            "hourly_rate": 0,
            "description": "A task description",
        }
    ],
    "contracts": [
        {
            "id": 458639048,
            "user_id": 933590696,
            "firstname": "Michael",
            "lastname": "Mustermann",
            "billable": True,
            "active": True,
            "budget": None,
            "hourly_rate": 0,
        }
    ],
    "project_group": {"id": 456687, "name": "Webpages"},
    "billing_contact": {"id": 1234, "firstname": "Maxine", "lastname": "Muster"},
    "contact": {"id": 2345, "firstname": "Max", "lastname": "Muster"},
    "secondary_contact": {"id": 3456, "firstname": "Meike", "lastname": "Muster"},
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}

ASSIGNED_PROJECT_JSON = {
    "id": 1234,
    "identifier": "P1900",
    "name": "Application",
    "active": False,
    "billable": True,
    "customer": {"id": 4567, "name": "A Company"},
    "tasks": [{"id": 573383, "name": "Integrations", "active": True, "billable": True}],
    "contract": {"user_id": 65455, "active": True},
}

REPORT_JSON = {
    "budget_total": 50000.0,
    "budget_progress_in_percentage": 50,
    "budget_remaining": 25.0,
    "invoiced_total": 27885.0,
    "currency": "EUR",
    "hours_total": 1500,
    "hours_billable": 1340,
    "hours_remaining": 1500,
    "costs_expenses": 4000.0,
    "costs_activities": 16450.0,
    "costs_by_task": [
        {"id": 7536, "name": "Project Management", "hours_total": 12.5, "total_costs": 725.0}
    ],
}

SHARE_JSON = {"id": 123, "active": True, "url": "https://..."}

PAGINATION_HEADERS = {"X-Page": "1", "X-Per-Page": "100", "X-Total": "1"}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def projects(client: Moco) -> Projects:
    return Projects(client._transport)


class TestProjectsList:
    @respx.mock
    def test_list_projects(self, projects: Projects) -> None:
        respx.get(f"{BASE}/projects").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([PROJECT_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = projects.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Project)
        assert page.items[0].name == "Website Support"

    @respx.mock
    def test_list_projects_with_filters(self, projects: Projects) -> None:
        respx.get(f"{BASE}/projects").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = projects.list(include_archived=True, leader_id=123)
        assert len(page.items) == 0


class TestProjectsAssigned:
    @respx.mock
    def test_assigned_projects(self, projects: Projects) -> None:
        respx.get(f"{BASE}/projects/assigned").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([ASSIGNED_PROJECT_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = projects.assigned()
        assert len(page.items) == 1
        assert isinstance(page.items[0], AssignedProject)
        assert page.items[0].name == "Application"


class TestProjectsGet:
    @respx.mock
    def test_get_project(self, projects: Projects) -> None:
        respx.get(f"{BASE}/projects/1234567").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PROJECT_JSON).encode()
            )
        )
        resp = projects.get(1234567)
        assert resp.parsed.id == 1234567
        assert resp.parsed.name == "Website Support"


class TestProjectsCreate:
    @respx.mock
    def test_create_project(self, projects: Projects) -> None:
        respx.post(f"{BASE}/projects").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PROJECT_JSON).encode()
            )
        )
        resp = projects.create(
            name="Website Support",
            currency="EUR",
            start_date="2018-01-01",
            finish_date="2018-12-31",
            fixed_price=True,
            retainer=False,
            leader_id=933590696,
            customer_id=1233434,
        )
        assert resp.parsed.name == "Website Support"


class TestProjectsUpdate:
    @respx.mock
    def test_update_project(self, projects: Projects) -> None:
        updated = {**PROJECT_JSON, "budget": 25000}
        respx.put(f"{BASE}/projects/1234567").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = projects.update(1234567, budget=25000)
        assert resp.parsed.budget == 25000


class TestProjectsDelete:
    @respx.mock
    def test_delete_project(self, projects: Projects) -> None:
        respx.delete(f"{BASE}/projects/1234567").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = projects.delete(1234567)
        assert resp.parsed is None


class TestProjectsArchive:
    @respx.mock
    def test_archive_project(self, projects: Projects) -> None:
        respx.put(f"{BASE}/projects/1234567/archive").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PROJECT_JSON).encode()
            )
        )
        resp = projects.archive(1234567)
        assert resp.parsed.id == 1234567

    @respx.mock
    def test_unarchive_project(self, projects: Projects) -> None:
        respx.put(f"{BASE}/projects/1234567/unarchive").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PROJECT_JSON).encode()
            )
        )
        resp = projects.unarchive(1234567)
        assert resp.parsed.id == 1234567


class TestProjectsReport:
    @respx.mock
    def test_report(self, projects: Projects) -> None:
        respx.get(f"{BASE}/projects/1234567/report").mock(
            return_value=httpx.Response(
                200, content=json.dumps(REPORT_JSON).encode()
            )
        )
        resp = projects.report(1234567)
        assert isinstance(resp.parsed, ProjectReport)
        assert resp.parsed.budget_total == 50000.0


class TestProjectsShare:
    @respx.mock
    def test_share(self, projects: Projects) -> None:
        respx.put(f"{BASE}/projects/1234567/share").mock(
            return_value=httpx.Response(
                200, content=json.dumps(SHARE_JSON).encode()
            )
        )
        resp = projects.share(1234567)
        assert isinstance(resp.parsed, ProjectShareResponse)
        assert resp.parsed.active is True

    @respx.mock
    def test_disable_share(self, projects: Projects) -> None:
        disabled = {"id": 123, "active": False, "url": None}
        respx.put(f"{BASE}/projects/1234567/disable_share").mock(
            return_value=httpx.Response(
                200, content=json.dumps(disabled).encode()
            )
        )
        resp = projects.disable_share(1234567)
        assert resp.parsed.active is False


class TestProjectsProjectGroup:
    @respx.mock
    def test_assign_project_group(self, projects: Projects) -> None:
        respx.put(f"{BASE}/projects/1234567/assign_project_group").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PROJECT_JSON).encode()
            )
        )
        resp = projects.assign_project_group(1234567, project_group_id=456687)
        assert resp.parsed.id == 1234567

    @respx.mock
    def test_unassign_project_group(self, projects: Projects) -> None:
        respx.put(f"{BASE}/projects/1234567/unassign_project_group").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PROJECT_JSON).encode()
            )
        )
        resp = projects.unassign_project_group(1234567)
        assert resp.parsed.id == 1234567
