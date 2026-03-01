"""Tests for the Project Expenses resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.project_expenses import ProjectExpenses
from moco_py.types.project_expenses import ProjectExpense

BASE = "https://test.mocoapp.com/api/v1"

EXPENSE_JSON = {
    "id": 47266,
    "date": "2024-06-07",
    "title": "Hosting XS",
    "description": "<div>Hosting, Monitoring und Backup</div>",
    "quantity": 3,
    "unit": "Monat",
    "unit_price": 29,
    "unit_cost": 19,
    "price": 87,
    "cost": 57,
    "currency": "CHF",
    "budget_relevant": True,
    "billable": True,
    "billed": False,
    "purchase_assignment_locked": True,
    "cost_total_planned": 0,
    "planned_purchase_date": None,
    "invoice_id": None,
    "recurring_expense_id": None,
    "service_period": "06/2024",
    "service_period_from": "2024-06-01",
    "service_period_to": "2024-06-30",
    "file_url": "https://example.com/beleg1.jpg",
    "revenue_category": {
        "id": 124,
        "name": "Hosting",
        "revenue_account": 30056,
        "cost_category": "HO1",
    },
    "custom_properties": {"Type": "Website"},
    "company": {"id": 1234, "name": "Acme Corp."},
    "project": {"id": 1234, "name": "Project A"},
    "group": {"id": 456, "title": "Expense Group A", "budget": 5200},
    "purchase_items": [],
    "created_at": "2024-06-06T09:33:46Z",
    "updated_at": "2024-06-06T09:33:46Z",
}

PAGINATION_HEADERS = {"X-Page": "1", "X-Per-Page": "100", "X-Total": "1"}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def resource(client: Moco) -> ProjectExpenses:
    return ProjectExpenses(client._transport)


class TestProjectExpensesList:
    @respx.mock
    def test_list_expenses(self, resource: ProjectExpenses) -> None:
        respx.get(f"{BASE}/projects/1/expenses").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([EXPENSE_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = resource.list(1)
        assert len(page.items) == 1
        assert isinstance(page.items[0], ProjectExpense)
        assert page.items[0].title == "Hosting XS"


class TestProjectExpensesListAll:
    @respx.mock
    def test_list_all_expenses(self, resource: ProjectExpenses) -> None:
        respx.get(f"{BASE}/projects/expenses").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([EXPENSE_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = resource.list_all()
        assert len(page.items) == 1


class TestProjectExpensesGet:
    @respx.mock
    def test_get_expense(self, resource: ProjectExpenses) -> None:
        respx.get(f"{BASE}/projects/1/expenses/47266").mock(
            return_value=httpx.Response(
                200, content=json.dumps(EXPENSE_JSON).encode()
            )
        )
        resp = resource.get(1, 47266)
        assert resp.parsed.id == 47266


class TestProjectExpensesCreate:
    @respx.mock
    def test_create_expense(self, resource: ProjectExpenses) -> None:
        respx.post(f"{BASE}/projects/1/expenses").mock(
            return_value=httpx.Response(
                200, content=json.dumps(EXPENSE_JSON).encode()
            )
        )
        resp = resource.create(
            1,
            date="2024-06-07",
            title="Hosting XS",
            quantity=3,
            unit="Monat",
            unit_price=29,
            unit_cost=19,
        )
        assert resp.parsed.title == "Hosting XS"


class TestProjectExpensesUpdate:
    @respx.mock
    def test_update_expense(self, resource: ProjectExpenses) -> None:
        updated = {**EXPENSE_JSON, "unit_price": 49}
        respx.put(f"{BASE}/projects/1/expenses/47266").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = resource.update(1, 47266, unit_price=49)
        assert resp.parsed.unit_price == 49


class TestProjectExpensesDelete:
    @respx.mock
    def test_delete_expense(self, resource: ProjectExpenses) -> None:
        respx.delete(f"{BASE}/projects/1/expenses/47266").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = resource.delete(1, 47266)
        assert resp.parsed is None


class TestProjectExpensesDisregard:
    @respx.mock
    def test_disregard_expenses(self, resource: ProjectExpenses) -> None:
        respx.post(f"{BASE}/projects/1/expenses/disregard").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = resource.disregard(1, expense_ids=[47266], reason="Courtesy")
        assert resp.parsed is None


class TestProjectExpensesBulk:
    @respx.mock
    def test_bulk_create(self, resource: ProjectExpenses) -> None:
        respx.post(f"{BASE}/projects/1/expenses/bulk").mock(
            return_value=httpx.Response(
                200, content=json.dumps([EXPENSE_JSON]).encode()
            )
        )
        resp = resource.bulk(
            1,
            bulk_data=[
                {
                    "date": "2024-06-07",
                    "title": "Hosting XS",
                    "quantity": 3,
                    "unit": "Monat",
                    "unit_price": 29,
                    "unit_cost": 19,
                }
            ],
        )
        assert resp.parsed is not None
