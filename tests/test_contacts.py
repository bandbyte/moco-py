"""Tests for the Contacts (People) resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.contacts import Contacts
from moco_py.types.contacts import Contact

BASE = "https://test.mocoapp.com/api/v1"

CONTACT_JSON = {
    "id": 123,
    "gender": "M",
    "firstname": "Peter",
    "lastname": "Muster",
    "title": "Dr. med.",
    "job_position": "Account Manager",
    "mobile_phone": "+41 123 45 67",
    "work_fax": "",
    "work_phone": "+41 445 45 67",
    "work_email": "peter.muster@beispiel.ch",
    "work_address": "Beispiel AG\nPeter Muster\nBeispielstrasse 123",
    "home_email": "",
    "home_address": "",
    "birthday": "1959-05-22",
    "info": "",
    "avatar_url": "https://meinefirma.mocoapp.com/.../profil.jpg",
    "tags": ["Key Account", "Christmas Card"],
    "company": {
        "id": 123456,
        "type": "customer",
        "name": "Beispiel AG",
    },
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def contacts(client: Moco) -> Contacts:
    return Contacts(client._transport)


class TestContactsList:
    @respx.mock
    def test_list_contacts(self, contacts: Contacts) -> None:
        respx.get(f"{BASE}/contacts/people").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([CONTACT_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = contacts.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Contact)
        assert page.items[0].lastname == "Muster"
        assert page.items[0].company is not None
        assert page.items[0].company.name == "Beispiel AG"

    @respx.mock
    def test_list_contacts_with_filters(self, contacts: Contacts) -> None:
        respx.get(f"{BASE}/contacts/people").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "0",
                },
            )
        )
        page = contacts.list(tags="Key Account", term="peter")
        assert len(page.items) == 0


class TestContactsGet:
    @respx.mock
    def test_get_contact(self, contacts: Contacts) -> None:
        respx.get(f"{BASE}/contacts/people/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(CONTACT_JSON).encode()
            )
        )
        resp = contacts.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.firstname == "Peter"


class TestContactsCreate:
    @respx.mock
    def test_create_contact(self, contacts: Contacts) -> None:
        respx.post(f"{BASE}/contacts/people").mock(
            return_value=httpx.Response(
                200, content=json.dumps(CONTACT_JSON).encode()
            )
        )
        resp = contacts.create(
            lastname="Muster", gender="M", firstname="Peter"
        )
        assert resp.parsed.lastname == "Muster"


class TestContactsUpdate:
    @respx.mock
    def test_update_contact(self, contacts: Contacts) -> None:
        updated = {**CONTACT_JSON, "job_position": "Head of Sales"}
        respx.put(f"{BASE}/contacts/people/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = contacts.update(123, job_position="Head of Sales")
        assert resp.parsed.job_position == "Head of Sales"


class TestContactsDelete:
    @respx.mock
    def test_delete_contact(self, contacts: Contacts) -> None:
        respx.delete(f"{BASE}/contacts/people/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = contacts.delete(123)
        assert resp.parsed is None
