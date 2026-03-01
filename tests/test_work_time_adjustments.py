"""Tests for the User Work Time Adjustments resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py._transport import SyncTransport
from moco_py.resources.work_time_adjustments import WorkTimeAdjustments
from moco_py.types.work_time_adjustments import WorkTimeAdjustment

BASE = "https://test.mocoapp.com/api/v1"

ADJUSTMENT_JSON = {
    "id": 1972,
    "date": "2022-01-01",
    "description": "Overtime from 2021",
    "hours": 172.01,
    "creator": {"id": 933590697, "firstname": "Jane", "lastname": "Doe"},
    "user": {"id": 933590696, "firstname": "John", "lastname": "Doe"},
    "created_at": "2022-01-02T17:31:00Z",
    "updated_at": "2022-01-02T17:31:00Z",
}


@pytest.fixture()
def work_time_adjustments() -> WorkTimeAdjustments:
    transport = SyncTransport(
        base_url=BASE, api_key="test-key", timeout=10, max_retries=0
    )
    return WorkTimeAdjustments(transport)


class TestWorkTimeAdjustmentsList:
    @respx.mock
    def test_list_adjustments(
        self, work_time_adjustments: WorkTimeAdjustments
    ) -> None:
        respx.get(f"{BASE}/users/work_time_adjustments").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([ADJUSTMENT_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = work_time_adjustments.list(user_id=933590696)
        assert len(page.items) == 1
        assert isinstance(page.items[0], WorkTimeAdjustment)
        assert page.items[0].description == "Overtime from 2021"


class TestWorkTimeAdjustmentsGet:
    @respx.mock
    def test_get_adjustment(
        self, work_time_adjustments: WorkTimeAdjustments
    ) -> None:
        respx.get(f"{BASE}/users/work_time_adjustments/1972").mock(
            return_value=httpx.Response(
                200, content=json.dumps(ADJUSTMENT_JSON).encode()
            )
        )
        resp = work_time_adjustments.get(1972)
        assert resp.parsed.id == 1972
        assert resp.parsed.hours == 172.01


class TestWorkTimeAdjustmentsCreate:
    @respx.mock
    def test_create_adjustment(
        self, work_time_adjustments: WorkTimeAdjustments
    ) -> None:
        respx.post(f"{BASE}/users/work_time_adjustments").mock(
            return_value=httpx.Response(
                200, content=json.dumps(ADJUSTMENT_JSON).encode()
            )
        )
        resp = work_time_adjustments.create(
            user_id=933590696,
            description="Overtime from 2021",
            date="2022-01-01",
            hours=172.01,
        )
        assert resp.parsed.description == "Overtime from 2021"


class TestWorkTimeAdjustmentsUpdate:
    @respx.mock
    def test_update_adjustment(
        self, work_time_adjustments: WorkTimeAdjustments
    ) -> None:
        updated = {**ADJUSTMENT_JSON, "description": "A new description"}
        respx.put(f"{BASE}/users/work_time_adjustments/1972").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = work_time_adjustments.update(
            1972, description="A new description"
        )
        assert resp.parsed.description == "A new description"


class TestWorkTimeAdjustmentsDelete:
    @respx.mock
    def test_delete_adjustment(
        self, work_time_adjustments: WorkTimeAdjustments
    ) -> None:
        respx.delete(f"{BASE}/users/work_time_adjustments/1972").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = work_time_adjustments.delete(1972)
        assert resp.parsed is None
