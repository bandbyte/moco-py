"""Tests for the Invoices resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.invoices import Invoices
from moco_py.types.invoices import Invoice, InvoiceExpense, InvoiceTimesheetActivity

BASE = "https://test.mocoapp.com/api/v1"

INVOICE_JSON = {
    "id": 80547,
    "customer_id": 760269602,
    "project_id": 944514545,
    "offer_id": 98375923,
    "identifier": "R1704-013",
    "date": "2017-04-05",
    "due_date": "2017-04-25",
    "service_period": "10/2018",
    "service_period_from": "2018-10-01",
    "service_period_to": "2018-10-31",
    "status": "paid",
    "reversed": False,
    "reversal_invoice_id": None,
    "reversal": False,
    "reversed_invoice_id": None,
    "title": "Invoice",
    "recipient_address": "Beispiel AG\r\nBeispielstrasse 123\r\n8000 Zürich",
    "currency": "CHF",
    "net_total": 35612.5,
    "tax": 8,
    "gross_total": 38461.5,
    "discount": 10,
    "locked": False,
    "activity_hours_modified": False,
    "tags": ["Postversand"],
    "user": {"id": 1234, "firstname": "Jane", "lastname": "Doe"},
    "items": [
        {
            "id": 387469,
            "type": "title",
            "title": "März 2017",
            "description": None,
            "quantity": None,
            "unit": None,
            "unit_price": None,
            "net_total": 0,
            "service_type": "service",
        }
    ],
    "payments": [
        {
            "id": 65938,
            "date": "2017-05-30",
            "paid_total": 10000,
            "currency": "CHF",
            "created_on": "2017-06-05",
            "updated_on": "2017-06-05",
        }
    ],
    "reminders": [],
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}

TIMESHEET_JSON = {
    "id": 988913748,
    "date": "2021-01-25",
    "hours": 4.0,
    "description": "Description",
    "billed": True,
    "billable": True,
    "tag": "",
    "remote_service": "trello",
    "remote_id": "0FhzirkJ",
    "remote_url": "https://trello.com/c/0FhziaBc/1-test",
    "project": {"id": 944807389, "name": "Pitch Project", "billable": True},
    "task": {"id": 2262446, "name": "Design / UX", "billable": True},
    "customer": {"id": 760255659, "name": "Acme Corp."},
    "user": {"id": 933618783, "firstname": "Jane", "lastname": "Doe"},
    "timer_started_at": None,
    "created_at": "2021-02-26T10:48:28Z",
    "updated_at": "2021-02-26T11:42:47Z",
    "hourly_rate": 150.0,
}

EXPENSE_JSON = {
    "id": 47266,
    "date": "2017-07-07",
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
    "recurring_expense_id": None,
    "service_period": "10/2020",
    "service_period_from": "2020-10-01",
    "service_period_to": "2020-10-31",
    "company": {"id": 1234, "name": "Acme Corp."},
    "project": {"id": 1234, "name": "Project A"},
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}

PAGINATION_HEADERS = {
    "X-Page": "1",
    "X-Per-Page": "100",
    "X-Total": "1",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def invoices(client: Moco) -> Invoices:
    return Invoices(client._transport)


class TestInvoicesList:
    @respx.mock
    def test_list_invoices(self, invoices: Invoices) -> None:
        respx.get(f"{BASE}/invoices").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([INVOICE_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = invoices.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Invoice)
        assert page.items[0].identifier == "R1704-013"

    @respx.mock
    def test_list_invoices_with_filters(self, invoices: Invoices) -> None:
        route = respx.get(f"{BASE}/invoices").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        invoices.list(status="paid", company_id=123)
        assert route.called
        request = route.calls[0].request
        assert b"status=paid" in request.url.query
        assert b"company_id=123" in request.url.query


class TestInvoicesLocked:
    @respx.mock
    def test_locked_invoices(self, invoices: Invoices) -> None:
        respx.get(f"{BASE}/invoices/locked").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([INVOICE_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = invoices.locked()
        assert len(page.items) == 1


class TestInvoicesGet:
    @respx.mock
    def test_get_invoice(self, invoices: Invoices) -> None:
        respx.get(f"{BASE}/invoices/80547").mock(
            return_value=httpx.Response(
                200, content=json.dumps(INVOICE_JSON).encode()
            )
        )
        resp = invoices.get(80547)
        assert resp.parsed.id == 80547
        assert resp.parsed.title == "Invoice"
        assert resp.parsed.items is not None
        assert len(resp.parsed.items) == 1


class TestInvoicesCreate:
    @respx.mock
    def test_create_invoice(self, invoices: Invoices) -> None:
        respx.post(f"{BASE}/invoices").mock(
            return_value=httpx.Response(
                200, content=json.dumps(INVOICE_JSON).encode()
            )
        )
        resp = invoices.create(
            customer_id=760269602,
            recipient_address="Beispiel AG",
            date="2017-04-05",
            due_date="2017-04-25",
            title="Invoice",
            tax=8.0,
            currency="CHF",
            items=[{"type": "item", "title": "Work", "quantity": 1, "unit": "h", "unit_price": 100}],
        )
        assert resp.parsed.id == 80547


class TestInvoicesTimesheet:
    @respx.mock
    def test_timesheet(self, invoices: Invoices) -> None:
        respx.get(f"{BASE}/invoices/80547/timesheet").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([TIMESHEET_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = invoices.timesheet(80547)
        assert len(page.items) == 1
        assert isinstance(page.items[0], InvoiceTimesheetActivity)
        assert page.items[0].hours == 4.0


class TestInvoicesExpenses:
    @respx.mock
    def test_expenses(self, invoices: Invoices) -> None:
        respx.get(f"{BASE}/invoices/80547/expenses").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([EXPENSE_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = invoices.expenses(80547)
        assert len(page.items) == 1
        assert isinstance(page.items[0], InvoiceExpense)
        assert page.items[0].title == "Hosting XS"


class TestInvoicesUpdateStatus:
    @respx.mock
    def test_update_status(self, invoices: Invoices) -> None:
        respx.put(f"{BASE}/invoices/80547/update_status").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = invoices.update_status(80547, status="sent")
        assert resp.parsed is None


class TestInvoicesSendEmail:
    @respx.mock
    def test_send_email(self, invoices: Invoices) -> None:
        respx.post(f"{BASE}/invoices/80547/send_email").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = invoices.send_email(
            80547, subject="Invoice", text="Kind regards"
        )
        assert resp.parsed is None


class TestInvoicesDelete:
    @respx.mock
    def test_delete_invoice(self, invoices: Invoices) -> None:
        respx.delete(f"{BASE}/invoices/80547").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = invoices.delete(80547, reason="Wrong number")
        assert resp.parsed is None
