"""Tests for the Project Recurring Expenses resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.project_recurring_expenses import ProjectRecurringExpenses
from moco_py.types.project_recurring_expenses import ProjectRecurringExpense

BASE = "https://test.mocoapp.com/api/v1"

RECURRING_EXPENSE_JSON = {
    "id": 47266,
    "start_date": "2017-07-01",
    "finish_date": "2017-12-31",
    "recur_next_date": "2017-09-01",
    "period": "monthly",
    "title": "Hosting XS",
    "description": "<div>Hosting, Monitoring und Backup</div>",
    "quantity": 1,
    "unit": "Server",
    "unit_price": 29,
    "unit_cost": 19,
    "price": 29,
    "cost": 19,
    "currency": "CHF",
    "budget_relevant": True,
    "billable": True,
    "service_period_direction": "forward",
    "custom_properties": {"Type": "Website"},
    "project": {"id": 1234, "name": "Project A"},
    "revenue_category": {
        "id": 124,
        "name": "Hosting",
        "revenue_account": 30056,
        "cost_category": "HO1",
    },
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}

PAGINATION_HEADERS = {"X-Page": "1", "X-Per-Page": "100", "X-Total": "1"}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def resource(client: Moco) -> ProjectRecurringExpenses:
    return ProjectRecurringExpenses(client._transport)


class TestRecurringExpensesList:
    @respx.mock
    def test_list_recurring_expenses(self, resource: ProjectRecurringExpenses) -> None:
        respx.get(f"{BASE}/projects/1/recurring_expenses").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([RECURRING_EXPENSE_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = resource.list(1)
        assert len(page.items) == 1
        assert isinstance(page.items[0], ProjectRecurringExpense)
        assert page.items[0].title == "Hosting XS"


class TestRecurringExpensesListAll:
    @respx.mock
    def test_list_all_recurring_expenses(
        self, resource: ProjectRecurringExpenses
    ) -> None:
        respx.get(f"{BASE}/recurring_expenses").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([RECURRING_EXPENSE_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = resource.list_all()
        assert len(page.items) == 1


class TestRecurringExpensesGet:
    @respx.mock
    def test_get_recurring_expense(
        self, resource: ProjectRecurringExpenses
    ) -> None:
        respx.get(f"{BASE}/projects/1/recurring_expenses/47266").mock(
            return_value=httpx.Response(
                200, content=json.dumps(RECURRING_EXPENSE_JSON).encode()
            )
        )
        resp = resource.get(1, 47266)
        assert resp.parsed.id == 47266


class TestRecurringExpensesCreate:
    @respx.mock
    def test_create_recurring_expense(
        self, resource: ProjectRecurringExpenses
    ) -> None:
        respx.post(f"{BASE}/projects/1/recurring_expenses").mock(
            return_value=httpx.Response(
                200, content=json.dumps(RECURRING_EXPENSE_JSON).encode()
            )
        )
        resp = resource.create(
            1,
            start_date="2017-07-01",
            period="monthly",
            title="Hosting XS",
            quantity=1,
            unit="Server",
            unit_price=29,
            unit_cost=19,
        )
        assert resp.parsed.title == "Hosting XS"


class TestRecurringExpensesUpdate:
    @respx.mock
    def test_update_recurring_expense(
        self, resource: ProjectRecurringExpenses
    ) -> None:
        updated = {**RECURRING_EXPENSE_JSON, "unit_price": 49}
        respx.put(f"{BASE}/projects/1/recurring_expenses/47266").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = resource.update(1, 47266, unit_price=49)
        assert resp.parsed.unit_price == 49


class TestRecurringExpensesRecur:
    @respx.mock
    def test_recur(self, resource: ProjectRecurringExpenses) -> None:
        respx.post(f"{BASE}/projects/1/recurring_expenses/47266/recur").mock(
            return_value=httpx.Response(
                200, content=json.dumps(RECURRING_EXPENSE_JSON).encode()
            )
        )
        resp = resource.recur(1, 47266)
        assert resp.parsed.id == 47266


class TestRecurringExpensesDelete:
    @respx.mock
    def test_delete_recurring_expense(
        self, resource: ProjectRecurringExpenses
    ) -> None:
        respx.delete(f"{BASE}/projects/1/recurring_expenses/47266").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = resource.delete(1, 47266)
        assert resp.parsed is None
