"""Tests for the Reports resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.reports import Reports
from moco_py.types.reports import (
    AbsenceEntry,
    CashflowEntry,
    FinanceEntry,
    PlannedVsTrackedEntry,
    UtilizationEntry,
)

BASE = "https://test.mocoapp.com/api/v1"

ABSENCE_JSON = {
    "user": {"id": 123, "firstname": "Jane", "lastname": "Doe"},
    "total_vacation_days": 25.0,
    "used_vacation_days": 10.5,
    "planned_vacation_days": 5.0,
    "sickdays": 4.0,
}

CASHFLOW_JSON = {
    "record_id": 28206351,
    "company_id": 760383472,
    "description": "R2212-022 Invoice",
    "user_id": 933622946,
    "amount_in_account_currency": 1022.07,
    "kind": "invoice_created",
    "company": {"id": 760683172, "name": "Kronenhalle Bar"},
    "user": {"id": 933622946, "firstname": "John", "lastname": "Doe"},
    "date": "2024-09-17",
}

FINANCE_JSON = {
    "record_id": 3731655,
    "company_id": 760718470,
    "description": "ZL 1",
    "user_id": 933621267,
    "net_amount_in_account_currency": 100.0,
    "kind": "incoming_expenses",
    "company": {"id": 762768470, "name": "Maus AG"},
    "user": {"id": 933621267, "firstname": "Jenni", "lastname": "Doe"},
    "date": "2025-03-27",
}

PLANNED_VS_TRACKED_JSON = {
    "user_id": 111,
    "project_id": 222,
    "tracked_hours": 0.0,
    "planned_hours": 218.0,
    "delta": -218.0,
    "quota": 0.0,
    "user": {
        "id": 111,
        "firstname": "John",
        "name": "Smith",
        "initials": "JS",
        "color": "#d9822b",
        "unit": {"id": 777, "name": "4 Support / Success"},
    },
    "project": {
        "id": 222,
        "identifier": "276",
        "name": "Support",
        "company": {"id": 333, "name": "hundertzehn GmbH"},
    },
}

UTILIZATION_JSON = {
    "date": "2025-08-20",
    "user_id": 92345,
    "target_hours": 6.4,
    "billable_hours": 4.3,
    "unbillable_hours": 0.83,
    "billable_seconds": 15487,
    "unbillable_seconds": 3000,
}

PAGINATED_HEADERS = {
    "X-Page": "1",
    "X-Per-Page": "100",
    "X-Total": "1",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def reports(client: Moco) -> Reports:
    return Reports(client._transport)


class TestReportsAbsences:
    @respx.mock
    def test_absences(self, reports: Reports) -> None:
        respx.get(f"{BASE}/report/absences").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([ABSENCE_JSON]).encode(),
                headers=PAGINATED_HEADERS,
            )
        )
        page = reports.absences()
        assert len(page.items) == 1
        assert isinstance(page.items[0], AbsenceEntry)
        assert page.items[0].total_vacation_days == 25.0

    @respx.mock
    def test_absences_with_filters(self, reports: Reports) -> None:
        respx.get(f"{BASE}/report/absences").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([]).encode(),
                headers=PAGINATED_HEADERS,
            )
        )
        page = reports.absences(active=True, year=2025)
        assert len(page.items) == 0


class TestReportsCashflow:
    @respx.mock
    def test_cashflow(self, reports: Reports) -> None:
        respx.get(f"{BASE}/report/cashflow").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([CASHFLOW_JSON]).encode(),
                headers=PAGINATED_HEADERS,
            )
        )
        page = reports.cashflow()
        assert len(page.items) == 1
        assert isinstance(page.items[0], CashflowEntry)
        assert page.items[0].kind == "invoice_created"


class TestReportsFinance:
    @respx.mock
    def test_finance(self, reports: Reports) -> None:
        respx.get(f"{BASE}/report/finance").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([FINANCE_JSON]).encode(),
                headers=PAGINATED_HEADERS,
            )
        )
        page = reports.finance()
        assert len(page.items) == 1
        assert isinstance(page.items[0], FinanceEntry)
        assert page.items[0].net_amount_in_account_currency == 100.0


class TestReportsPlannedVsTracked:
    @respx.mock
    def test_planned_vs_tracked(self, reports: Reports) -> None:
        respx.get(f"{BASE}/report/planned_vs_tracked").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([PLANNED_VS_TRACKED_JSON]).encode(),
                headers=PAGINATED_HEADERS,
            )
        )
        page = reports.planned_vs_tracked()
        assert len(page.items) == 1
        assert isinstance(page.items[0], PlannedVsTrackedEntry)
        assert page.items[0].planned_hours == 218.0


class TestReportsUtilization:
    @respx.mock
    def test_utilization(self, reports: Reports) -> None:
        respx.get(f"{BASE}/report/utilization").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([UTILIZATION_JSON]).encode(),
                headers=PAGINATED_HEADERS,
            )
        )
        page = reports.utilization()
        assert len(page.items) == 1
        assert isinstance(page.items[0], UtilizationEntry)
        assert page.items[0].target_hours == 6.4
