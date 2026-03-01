"""Tests for the User Presences resource."""

from __future__ import annotations

import datetime
import json

import httpx
import pytest
import respx

from moco_py._transport import SyncTransport
from moco_py.resources.presences import Presences
from moco_py.types.presences import Presence

BASE = "https://test.mocoapp.com/api/v1"

PRESENCE_JSON = {
    "id": 982237015,
    "date": "2018-07-03",
    "from": "07:30",
    "to": "13:15",
    "is_home_office": True,
    "user": {"id": 933590696, "firstname": "John", "lastname": "Doe"},
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def presences() -> Presences:
    transport = SyncTransport(
        base_url=BASE, api_key="test-key", timeout=10, max_retries=0
    )
    return Presences(transport)


class TestPresencesList:
    @respx.mock
    def test_list_presences(self, presences: Presences) -> None:
        respx.get(f"{BASE}/users/presences").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([PRESENCE_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = presences.list(from_date="2018-06-01", to="2018-06-30")
        assert len(page.items) == 1
        assert isinstance(page.items[0], Presence)
        assert page.items[0].from_time == datetime.time(7, 30)


class TestPresencesGet:
    @respx.mock
    def test_get_presence(self, presences: Presences) -> None:
        respx.get(f"{BASE}/users/presences/982237015").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PRESENCE_JSON).encode()
            )
        )
        resp = presences.get(982237015)
        assert resp.parsed.id == 982237015
        assert resp.parsed.is_home_office is True


class TestPresencesCreate:
    @respx.mock
    def test_create_presence(self, presences: Presences) -> None:
        respx.post(f"{BASE}/users/presences").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PRESENCE_JSON).encode()
            )
        )
        resp = presences.create(
            date="2018-07-03", from_time="07:30", to="13:15"
        )
        assert resp.parsed.date == datetime.date(2018, 7, 3)


class TestPresencesTouch:
    @respx.mock
    def test_touch_presence(self, presences: Presences) -> None:
        respx.post(f"{BASE}/users/presences/touch").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PRESENCE_JSON).encode()
            )
        )
        resp = presences.touch()
        assert resp.parsed.id == 982237015


class TestPresencesUpdate:
    @respx.mock
    def test_update_presence(self, presences: Presences) -> None:
        updated = {**PRESENCE_JSON, "to": "14:00"}
        respx.put(f"{BASE}/users/presences/982237015").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = presences.update(982237015, to="14:00")
        assert resp.parsed.to == datetime.time(14, 0)


class TestPresencesDelete:
    @respx.mock
    def test_delete_presence(self, presences: Presences) -> None:
        respx.delete(f"{BASE}/users/presences/982237015").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = presences.delete(982237015)
        assert resp.parsed is None
