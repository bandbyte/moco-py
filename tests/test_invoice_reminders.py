"""Tests for the Invoice Reminders resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.invoice_reminders import InvoiceReminders
from moco_py.types.invoice_reminders import InvoiceReminder

BASE = "https://test.mocoapp.com/api/v1"

REMINDER_JSON = {
    "id": 1,
    "title": "Zahlungserinnerung",
    "text": "Bei der Bearbeitung unserer Buchhaltung...",
    "fee": 0.0,
    "date": "2019-10-16",
    "due_date": "2019-10-30",
    "status": "created",
    "file_url": "https://...",
    "invoice": {
        "id": 1489,
        "identifier": "1409-019",
        "title": "Rechnung - Android Prototype",
    },
    "created_at": "2019-10-30T07:20:40Z",
    "updated_at": "2020-03-19T09:13:44Z",
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
def invoice_reminders(client: Moco) -> InvoiceReminders:
    return InvoiceReminders(client._transport)


class TestInvoiceRemindersList:
    @respx.mock
    def test_list_reminders(self, invoice_reminders: InvoiceReminders) -> None:
        respx.get(f"{BASE}/invoice_reminders").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([REMINDER_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = invoice_reminders.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], InvoiceReminder)
        assert page.items[0].title == "Zahlungserinnerung"


class TestInvoiceRemindersGet:
    @respx.mock
    def test_get_reminder(self, invoice_reminders: InvoiceReminders) -> None:
        respx.get(f"{BASE}/invoice_reminders/1").mock(
            return_value=httpx.Response(
                200, content=json.dumps(REMINDER_JSON).encode()
            )
        )
        resp = invoice_reminders.get(1)
        assert resp.parsed.id == 1
        assert resp.parsed.invoice is not None
        assert resp.parsed.invoice.id == 1489


class TestInvoiceRemindersCreate:
    @respx.mock
    def test_create_reminder(self, invoice_reminders: InvoiceReminders) -> None:
        respx.post(f"{BASE}/invoice_reminders").mock(
            return_value=httpx.Response(
                200, content=json.dumps(REMINDER_JSON).encode()
            )
        )
        resp = invoice_reminders.create(
            invoice_id=1489, title="Zahlungserinnerung"
        )
        assert resp.parsed.id == 1


class TestInvoiceRemindersDelete:
    @respx.mock
    def test_delete_reminder(self, invoice_reminders: InvoiceReminders) -> None:
        respx.delete(f"{BASE}/invoice_reminders/1").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = invoice_reminders.delete(1)
        assert resp.parsed is None


class TestInvoiceRemindersSendEmail:
    @respx.mock
    def test_send_email(self, invoice_reminders: InvoiceReminders) -> None:
        respx.post(f"{BASE}/invoice_reminders/1/send_email").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = invoice_reminders.send_email(
            1, subject="Reminder", text="Please pay"
        )
        assert resp.parsed is None
