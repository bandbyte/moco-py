"""Tests for the Planning Entries resource."""

from __future__ import annotations

import datetime
import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.planning_entries import PlanningEntries
from moco_py.types.planning_entries import PlanningEntry

BASE = "https://test.mocoapp.com/api/v1"

PLANNING_ENTRY_JSON = {
    "id": 4839,
    "title": "Project Management",
    "starts_on": "2020-05-04",
    "ends_on": "2020-05-04",
    "hours_per_day": 6.0,
    "comment": "",
    "symbol": None,
    "color": "#2965cc",
    "read_only": False,
    "user": {
        "id": 5484,
        "firstname": "Thomas",
        "lastname": "Munster",
    },
    "project": {
        "id": 4553,
        "identifier": "130",
        "name": "Support",
        "customer_name": "Acme GmbH",
        "color": "#faeb44",
    },
    "task": {"id": 6789, "name": "Projektleitung"},
    "deal": None,
    "series_id": None,
    "tentative": False,
    "series_repeat": None,
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def planning_entries(client: Moco) -> PlanningEntries:
    return PlanningEntries(client._transport)


class TestPlanningEntriesList:
    @respx.mock
    def test_list_planning_entries(
        self, planning_entries: PlanningEntries
    ) -> None:
        respx.get(f"{BASE}/planning_entries").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([PLANNING_ENTRY_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = planning_entries.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], PlanningEntry)
        assert page.items[0].title == "Project Management"
        assert page.items[0].hours_per_day == 6.0

    @respx.mock
    def test_list_planning_entries_with_filters(
        self, planning_entries: PlanningEntries
    ) -> None:
        respx.get(f"{BASE}/planning_entries").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "0",
                },
            )
        )
        page = planning_entries.list(
            period="2020-05-01:2020-07-31", user_id=5484
        )
        assert len(page.items) == 0


class TestPlanningEntriesGet:
    @respx.mock
    def test_get_planning_entry(
        self, planning_entries: PlanningEntries
    ) -> None:
        respx.get(f"{BASE}/planning_entries/4839").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PLANNING_ENTRY_JSON).encode()
            )
        )
        resp = planning_entries.get(4839)
        assert resp.parsed.id == 4839
        assert resp.parsed.project is not None
        assert resp.parsed.project.name == "Support"


class TestPlanningEntriesCreate:
    @respx.mock
    def test_create_planning_entry(
        self, planning_entries: PlanningEntries
    ) -> None:
        respx.post(f"{BASE}/planning_entries").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PLANNING_ENTRY_JSON).encode()
            )
        )
        resp = planning_entries.create(
            project_id=4553,
            starts_on="2020-05-04",
            ends_on="2020-05-04",
            hours_per_day=6.0,
        )
        assert resp.parsed.starts_on == datetime.date(2020, 5, 4)


class TestPlanningEntriesUpdate:
    @respx.mock
    def test_update_planning_entry(
        self, planning_entries: PlanningEntries
    ) -> None:
        updated = {**PLANNING_ENTRY_JSON, "hours_per_day": 5.0}
        respx.put(f"{BASE}/planning_entries/4839").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = planning_entries.update(4839, hours_per_day=5.0)
        assert resp.parsed.hours_per_day == 5.0


class TestPlanningEntriesDelete:
    @respx.mock
    def test_delete_planning_entry(
        self, planning_entries: PlanningEntries
    ) -> None:
        respx.delete(f"{BASE}/planning_entries/4839").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = planning_entries.delete(4839)
        assert resp.parsed is None
