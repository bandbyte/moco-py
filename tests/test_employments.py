"""Tests for the User Employments resource."""

from __future__ import annotations

import datetime
import json

import httpx
import pytest
import respx

from moco_py._transport import SyncTransport
from moco_py.resources.employments import Employments
from moco_py.types.employments import Employment, EmploymentPattern

BASE = "https://test.mocoapp.com/api/v1"

EMPLOYMENT_JSON = {
    "id": 982237015,
    "weekly_target_hours": 29.75,
    "pattern": {
        "am": [0, 4.25, 4.25, 4.25, 4.25],
        "pm": [0, 4.25, 4.25, 4.25, 0],
    },
    "from": "2017-01-01",
    "to": None,
    "user": {"id": 933590696, "firstname": "John", "lastname": "Doe"},
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def employments() -> Employments:
    transport = SyncTransport(
        base_url=BASE, api_key="test-key", timeout=10, max_retries=0
    )
    return Employments(transport)


class TestEmploymentsList:
    @respx.mock
    def test_list_employments(self, employments: Employments) -> None:
        respx.get(f"{BASE}/users/employments").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([EMPLOYMENT_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = employments.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Employment)
        assert page.items[0].weekly_target_hours == 29.75
        assert page.items[0].from_date == datetime.date(2017, 1, 1)


class TestEmploymentsGet:
    @respx.mock
    def test_get_employment(self, employments: Employments) -> None:
        respx.get(f"{BASE}/users/employments/982237015").mock(
            return_value=httpx.Response(
                200, content=json.dumps(EMPLOYMENT_JSON).encode()
            )
        )
        resp = employments.get(982237015)
        assert resp.parsed.id == 982237015
        assert resp.parsed.pattern.am == [0, 4.25, 4.25, 4.25, 4.25]


class TestEmploymentsCreate:
    @respx.mock
    def test_create_employment(self, employments: Employments) -> None:
        respx.post(f"{BASE}/users/employments").mock(
            return_value=httpx.Response(
                200, content=json.dumps(EMPLOYMENT_JSON).encode()
            )
        )
        pattern = EmploymentPattern(
            am=[0, 4.25, 4.25, 4.25, 4.25],
            pm=[0, 4.25, 4.25, 4.25, 0],
        )
        resp = employments.create(
            user_id=933590696, pattern=pattern, from_date="2017-01-01"
        )
        assert resp.parsed.weekly_target_hours == 29.75


class TestEmploymentsUpdate:
    @respx.mock
    def test_update_employment(self, employments: Employments) -> None:
        respx.put(f"{BASE}/users/employments/982237015").mock(
            return_value=httpx.Response(
                200, content=json.dumps(EMPLOYMENT_JSON).encode()
            )
        )
        pattern = EmploymentPattern(
            am=[0, 4, 4, 4, 4],
            pm=[0, 4, 4, 4, 4],
        )
        resp = employments.update(982237015, pattern=pattern)
        assert resp.parsed.id == 982237015


class TestEmploymentsDelete:
    @respx.mock
    def test_delete_employment(self, employments: Employments) -> None:
        respx.delete(f"{BASE}/users/employments/982237015").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = employments.delete(982237015)
        assert resp.parsed is None
