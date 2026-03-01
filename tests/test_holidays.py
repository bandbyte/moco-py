"""Tests for the User Holidays resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py._transport import SyncTransport
from moco_py.resources.holidays import Holidays
from moco_py.types.holidays import Holiday

BASE = "https://test.mocoapp.com/api/v1"

HOLIDAY_JSON = {
    "id": 12345,
    "year": 2019,
    "title": "Urlaubsanspruch 80%",
    "days": 20,
    "hours": 160,
    "user": {"id": 933590696, "firstname": "John", "lastname": "Doe"},
    "creator": {"id": 933590697, "firstname": "Jane", "lastname": "Doe"},
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def holidays() -> Holidays:
    transport = SyncTransport(
        base_url=BASE, api_key="test-key", timeout=10, max_retries=0
    )
    return Holidays(transport)


class TestHolidaysList:
    @respx.mock
    def test_list_holidays(self, holidays: Holidays) -> None:
        respx.get(f"{BASE}/users/holidays").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([HOLIDAY_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = holidays.list(year=2019)
        assert len(page.items) == 1
        assert isinstance(page.items[0], Holiday)
        assert page.items[0].title == "Urlaubsanspruch 80%"


class TestHolidaysGet:
    @respx.mock
    def test_get_holiday(self, holidays: Holidays) -> None:
        respx.get(f"{BASE}/users/holidays/12345").mock(
            return_value=httpx.Response(
                200, content=json.dumps(HOLIDAY_JSON).encode()
            )
        )
        resp = holidays.get(12345)
        assert resp.parsed.id == 12345
        assert resp.parsed.days == 20


class TestHolidaysCreate:
    @respx.mock
    def test_create_holiday(self, holidays: Holidays) -> None:
        respx.post(f"{BASE}/users/holidays").mock(
            return_value=httpx.Response(
                200, content=json.dumps(HOLIDAY_JSON).encode()
            )
        )
        resp = holidays.create(
            year=2019,
            title="Urlaubsanspruch 80%",
            days=20,
            user_id=933590696,
        )
        assert resp.parsed.year == 2019


class TestHolidaysUpdate:
    @respx.mock
    def test_update_holiday(self, holidays: Holidays) -> None:
        updated = {**HOLIDAY_JSON, "days": 22}
        respx.put(f"{BASE}/users/holidays/12345").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = holidays.update(12345, days=22)
        assert resp.parsed.days == 22


class TestHolidaysDelete:
    @respx.mock
    def test_delete_holiday(self, holidays: Holidays) -> None:
        respx.delete(f"{BASE}/users/holidays/12345").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = holidays.delete(12345)
        assert resp.parsed is None
