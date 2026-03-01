"""Tests for the Project Payment Schedules resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.project_payment_schedules import ProjectPaymentSchedules
from moco_py.types.project_payment_schedules import ProjectPaymentSchedule

BASE = "https://test.mocoapp.com/api/v1"

SCHEDULE_JSON = {
    "id": 760153573,
    "date": "2017-04-05",
    "title": "Erste Anzahlung",
    "description": "<div>A description for this payment schedule</div>",
    "net_total": 1000,
    "project": {"id": 822322322, "identifier": "P0077", "name": "New website"},
    "checked": False,
    "billed": False,
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}

PAGINATION_HEADERS = {"X-Page": "1", "X-Per-Page": "100", "X-Total": "1"}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def resource(client: Moco) -> ProjectPaymentSchedules:
    return ProjectPaymentSchedules(client._transport)


class TestPaymentSchedulesList:
    @respx.mock
    def test_list_schedules(self, resource: ProjectPaymentSchedules) -> None:
        respx.get(f"{BASE}/projects/1/payment_schedules").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([SCHEDULE_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = resource.list(1)
        assert len(page.items) == 1
        assert isinstance(page.items[0], ProjectPaymentSchedule)
        assert page.items[0].title == "Erste Anzahlung"


class TestPaymentSchedulesListAll:
    @respx.mock
    def test_list_all_schedules(self, resource: ProjectPaymentSchedules) -> None:
        respx.get(f"{BASE}/projects/payment_schedules").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([SCHEDULE_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = resource.list_all()
        assert len(page.items) == 1


class TestPaymentSchedulesGet:
    @respx.mock
    def test_get_schedule(self, resource: ProjectPaymentSchedules) -> None:
        respx.get(f"{BASE}/projects/1/payment_schedules/760153573").mock(
            return_value=httpx.Response(
                200, content=json.dumps(SCHEDULE_JSON).encode()
            )
        )
        resp = resource.get(1, 760153573)
        assert resp.parsed.id == 760153573


class TestPaymentSchedulesCreate:
    @respx.mock
    def test_create_schedule(self, resource: ProjectPaymentSchedules) -> None:
        respx.post(f"{BASE}/projects/1/payment_schedules").mock(
            return_value=httpx.Response(
                200, content=json.dumps(SCHEDULE_JSON).encode()
            )
        )
        resp = resource.create(1, net_total=1000, date="2017-04-05", title="Erste Anzahlung")
        assert resp.parsed.net_total == 1000


class TestPaymentSchedulesUpdate:
    @respx.mock
    def test_update_schedule(self, resource: ProjectPaymentSchedules) -> None:
        updated = {**SCHEDULE_JSON, "checked": True}
        respx.put(f"{BASE}/projects/1/payment_schedules/760153573").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = resource.update(1, 760153573, checked=True)
        assert resp.parsed.checked is True


class TestPaymentSchedulesDelete:
    @respx.mock
    def test_delete_schedule(self, resource: ProjectPaymentSchedules) -> None:
        respx.delete(f"{BASE}/projects/1/payment_schedules/760153573").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = resource.delete(1, 760153573)
        assert resp.parsed is None
