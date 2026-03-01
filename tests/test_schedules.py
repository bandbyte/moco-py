"""Tests for the Schedules (Absences) resource."""

from __future__ import annotations

import datetime
import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.types.schedules import Schedule

BASE = "https://test.mocoapp.com/api/v1"

SCHEDULE_JSON = {
    "id": 123,
    "date": "2017-06-14",
    "comment": "Half day off",
    "am": True,
    "pm": True,
    "symbol": None,
    "assignment": {
        "id": 789,
        "name": "Holiday",
        "code": "4",
        "customer_name": "hundertzehn GmbH",
        "color": "#BBB",
        "type": "Absence",
    },
    "user": {
        "id": 567,
        "firstname": "Sabine",
        "lastname": "Schäuble",
    },
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


class TestSchedulesList:
    @respx.mock
    def test_list_schedules(self, client: Moco) -> None:
        respx.get(f"{BASE}/schedules").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([SCHEDULE_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = client.schedules.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Schedule)
        assert page.items[0].date == datetime.date(2017, 6, 14)
        assert page.items[0].assignment.name == "Holiday"
        assert page.items[0].user.firstname == "Sabine"

    @respx.mock
    def test_list_schedules_with_filters(self, client: Moco) -> None:
        respx.get(
            f"{BASE}/schedules",
            params={"from": "2018-10-01", "to": "2018-10-31", "user_id": "567"},
        ).mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([SCHEDULE_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = client.schedules.list(
            from_date="2018-10-01", to_date="2018-10-31", user_id=567
        )
        assert len(page.items) == 1


class TestSchedulesGet:
    @respx.mock
    def test_get_schedule(self, client: Moco) -> None:
        respx.get(f"{BASE}/schedules/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(SCHEDULE_JSON).encode()
            )
        )
        resp = client.schedules.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.comment == "Half day off"


class TestSchedulesCreate:
    @respx.mock
    def test_create_schedule(self, client: Moco) -> None:
        respx.post(f"{BASE}/schedules").mock(
            return_value=httpx.Response(
                200, content=json.dumps(SCHEDULE_JSON).encode()
            )
        )
        resp = client.schedules.create(date="2017-06-14", absence_code=4)
        assert resp.parsed.date == datetime.date(2017, 6, 14)
        assert resp.parsed.am is True


class TestSchedulesUpdate:
    @respx.mock
    def test_update_schedule(self, client: Moco) -> None:
        updated = {**SCHEDULE_JSON, "comment": "Full day off"}
        respx.put(f"{BASE}/schedules/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = client.schedules.update(123, comment="Full day off")
        assert resp.parsed.comment == "Full day off"


class TestSchedulesDelete:
    @respx.mock
    def test_delete_schedule(self, client: Moco) -> None:
        respx.delete(f"{BASE}/schedules/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = client.schedules.delete(123)
        assert resp.parsed is None
