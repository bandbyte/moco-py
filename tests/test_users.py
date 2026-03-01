"""Tests for the Users resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py._transport import SyncTransport
from moco_py.resources.users import Users
from moco_py.types.users import PerformanceReport, User

BASE = "https://test.mocoapp.com/api/v1"

USER_JSON = {
    "id": 123,
    "firstname": "Max",
    "lastname": "Muster",
    "active": True,
    "extern": False,
    "email": "max.muster@beispiel.de",
    "mobile_phone": "+49 177 123 45 67",
    "work_phone": "+49 40 123 45 67",
    "home_address": "",
    "info": "",
    "birthday": "1970-01-01",
    "iban": "CH3181239000001245689",
    "avatar_url": "https://meinefirma.mocoapp.com/.../profil.jpg",
    "tags": ["Deutschland"],
    "custom_properties": {"Starting Month": "January 2015"},
    "unit": {"id": 456, "name": "Geschäftsleitung"},
    "role": {"id": 42, "name": "Entwickler"},
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}

PERFORMANCE_REPORT_JSON = {
    "annually": {
        "year": 2021,
        "employment_hours": 1670.4,
        "target_hours": 1606.4,
        "hours_tracked_total": 210.95,
        "variation": -1395.45,
        "variation_until_today": -0.25,
        "hours_billable_total": 190.95,
    },
    "monthly": [
        {
            "year": 2021,
            "month": 1,
            "target_hours": 128.0,
            "hours_tracked_total": 133.71,
            "variation": 5.71,
            "hours_billable_total": 113.95,
        },
    ],
}


@pytest.fixture()
def users() -> Users:
    transport = SyncTransport(
        base_url=BASE, api_key="test-key", timeout=10, max_retries=0
    )
    return Users(transport)


class TestUsersList:
    @respx.mock
    def test_list_users(self, users: Users) -> None:
        respx.get(f"{BASE}/users").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([USER_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = users.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], User)
        assert page.items[0].firstname == "Max"
        assert page.items[0].unit.name == "Geschäftsleitung"


class TestUsersGet:
    @respx.mock
    def test_get_user(self, users: Users) -> None:
        respx.get(f"{BASE}/users/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(USER_JSON).encode()
            )
        )
        resp = users.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.lastname == "Muster"


class TestUsersCreate:
    @respx.mock
    def test_create_user(self, users: Users) -> None:
        respx.post(f"{BASE}/users").mock(
            return_value=httpx.Response(
                200, content=json.dumps(USER_JSON).encode()
            )
        )
        resp = users.create(
            firstname="Max",
            lastname="Muster",
            email="max.muster@beispiel.de",
            unit_id=456,
        )
        assert resp.parsed.firstname == "Max"


class TestUsersUpdate:
    @respx.mock
    def test_update_user(self, users: Users) -> None:
        updated = {**USER_JSON, "lastname": "Casanova"}
        respx.put(f"{BASE}/users/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = users.update(123, lastname="Casanova")
        assert resp.parsed.lastname == "Casanova"


class TestUsersDelete:
    @respx.mock
    def test_delete_user(self, users: Users) -> None:
        respx.delete(f"{BASE}/users/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = users.delete(123)
        assert resp.parsed is None


class TestUsersPerformanceReport:
    @respx.mock
    def test_performance_report(self, users: Users) -> None:
        respx.get(f"{BASE}/users/123/performance_report").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps(PERFORMANCE_REPORT_JSON).encode(),
            )
        )
        resp = users.performance_report(123)
        assert isinstance(resp.parsed, PerformanceReport)
        assert resp.parsed.annually.year == 2021
        assert len(resp.parsed.monthly) == 1
        assert resp.parsed.monthly[0].month == 1
