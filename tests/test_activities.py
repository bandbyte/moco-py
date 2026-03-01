"""Tests for the Activities resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.activities import Activities
from moco_py.types.activities import Activity

BASE = "https://test.mocoapp.com/api/v1"

ACTIVITY_JSON = {
    "id": 982237015,
    "date": "2018-07-03",
    "hours": 1.25,
    "seconds": 4500,
    "worked_seconds": 4500,
    "description": "Analysis context and dependencies",
    "billed": False,
    "invoice_id": None,
    "billable": False,
    "tag": "",
    "remote_service": "trello",
    "remote_id": "9qzOS8AA",
    "remote_url": "https://trello.com/c/9qzOS8AA/123-analyse",
    "project": {"id": 944587499, "name": "Website Relaunch", "billable": False},
    "task": {"id": 658636, "name": "Concept", "billable": False},
    "customer": {"id": 760253684, "name": "Example Inc."},
    "user": {"id": 933590696, "firstname": "John", "lastname": "Doe"},
    "hourly_rate": 150,
    "timer_started_at": None,
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def activities(client: Moco) -> Activities:
    return Activities(client._transport)


class TestActivitiesList:
    @respx.mock
    def test_list_activities(self, activities: Activities) -> None:
        respx.get(f"{BASE}/activities").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([ACTIVITY_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = activities.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Activity)
        assert page.items[0].description == "Analysis context and dependencies"

    @respx.mock
    def test_list_activities_with_filters(self, activities: Activities) -> None:
        respx.get(f"{BASE}/activities").mock(
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
        page = activities.list(
            from_date="2018-06-01",
            to_date="2018-06-30",
            project_id=4242,
        )
        assert len(page.items) == 0


class TestActivitiesGet:
    @respx.mock
    def test_get_activity(self, activities: Activities) -> None:
        respx.get(f"{BASE}/activities/982237015").mock(
            return_value=httpx.Response(
                200, content=json.dumps(ACTIVITY_JSON).encode()
            )
        )
        resp = activities.get(982237015)
        assert resp.parsed.id == 982237015
        assert resp.parsed.project.name == "Website Relaunch"


class TestActivitiesCreate:
    @respx.mock
    def test_create_activity(self, activities: Activities) -> None:
        respx.post(f"{BASE}/activities").mock(
            return_value=httpx.Response(
                200, content=json.dumps(ACTIVITY_JSON).encode()
            )
        )
        resp = activities.create(
            date="2018-07-03",
            project_id=944587499,
            task_id=658636,
            seconds=4500,
            description="Analysis context and dependencies",
        )
        assert resp.parsed.id == 982237015


class TestActivitiesBulkCreate:
    @respx.mock
    def test_bulk_create_activities(self, activities: Activities) -> None:
        respx.post(f"{BASE}/activities/bulk").mock(
            return_value=httpx.Response(
                200, content=json.dumps([ACTIVITY_JSON]).encode()
            )
        )
        resp = activities.bulk_create(
            activities=[
                {
                    "date": "2018-07-03",
                    "project_id": 944587499,
                    "task_id": 658636,
                    "seconds": 4500,
                }
            ]
        )
        assert resp.parsed[0].id == 982237015


class TestActivitiesUpdate:
    @respx.mock
    def test_update_activity(self, activities: Activities) -> None:
        updated = {**ACTIVITY_JSON, "seconds": 7200}
        respx.put(f"{BASE}/activities/982237015").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = activities.update(982237015, seconds=7200)
        assert resp.parsed.seconds == 7200


class TestActivitiesDelete:
    @respx.mock
    def test_delete_activity(self, activities: Activities) -> None:
        respx.delete(f"{BASE}/activities/982237015").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = activities.delete(982237015)
        assert resp.parsed is None


class TestActivitiesStartTimer:
    @respx.mock
    def test_start_timer(self, activities: Activities) -> None:
        timer_json = {**ACTIVITY_JSON, "timer_started_at": "2018-10-17T10:00:00Z"}
        respx.patch(f"{BASE}/activities/982237015/start_timer").mock(
            return_value=httpx.Response(
                200, content=json.dumps(timer_json).encode()
            )
        )
        resp = activities.start_timer(982237015)
        assert resp.parsed.timer_started_at == "2018-10-17T10:00:00Z"


class TestActivitiesStopTimer:
    @respx.mock
    def test_stop_timer(self, activities: Activities) -> None:
        respx.patch(f"{BASE}/activities/982237015/stop_timer").mock(
            return_value=httpx.Response(
                200, content=json.dumps(ACTIVITY_JSON).encode()
            )
        )
        resp = activities.stop_timer(982237015)
        assert resp.parsed.timer_started_at is None


class TestActivitiesDisregard:
    @respx.mock
    def test_disregard(self, activities: Activities) -> None:
        respx.post(f"{BASE}/activities/disregard").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = activities.disregard(
            reason="Courtesy service",
            activity_ids=[982237015],
            company_id=760253684,
        )
        assert resp.parsed is None
