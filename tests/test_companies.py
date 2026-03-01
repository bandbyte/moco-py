"""Tests for the Companies resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.companies import Companies
from moco_py.types.companies import Company

BASE = "https://test.mocoapp.com/api/v1"

COMPANY_JSON = {
    "id": 760253573,
    "type": "customer",
    "name": "Beispiel AG",
    "website": "www.beispiel-ag.com",
    "email": "info@beispiel-ag.com",
    "billing_email_cc": "cc@beispiel-ag.com",
    "phone": "+49 30 123 45 67",
    "fax": "+49 30 123 45 66",
    "address": "Beispiel AG\nBeispielstrasse 123\n12345 Beispielstadt",
    "tags": ["Netzwerk", "Druckerei"],
    "user": {"id": 933589840, "firstname": "Tobias", "lastname": "Miesel"},
    "info": "",
    "custom_properties": {"UID": "1234-UID-4567"},
    "identifier": "36",
    "intern": False,
    "billing_tax": 0,
    "currency": "CHF",
    "custom_rates": False,
    "include_time_report": False,
    "billing_notes": "Vor Rechnungsstellung PO beantragen.",
    "default_discount": 0.0,
    "default_cash_discount": 2.0,
    "default_cash_discount_days": 10,
    "country_code": "CH",
    "vat_identifier": "CH999999999",
    "alternative_correspondence_language": False,
    "default_invoice_due_days": 30,
    "footer": "<div>Footer text</div>",
    "projects": [
        {
            "id": 944504145,
            "identifier": "46",
            "name": "Layoutanpassung",
            "active": False,
            "billable": True,
        }
    ],
    "active": True,
    "archived_on": None,
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
    "debit_number": 10000,
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def companies(client: Moco) -> Companies:
    return Companies(client._transport)


class TestCompaniesList:
    @respx.mock
    def test_list_companies(self, companies: Companies) -> None:
        respx.get(f"{BASE}/companies").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([COMPANY_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = companies.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Company)
        assert page.items[0].name == "Beispiel AG"

    @respx.mock
    def test_list_companies_with_filters(self, companies: Companies) -> None:
        respx.get(f"{BASE}/companies").mock(
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
        page = companies.list(type="customer", term="beispiel")
        assert len(page.items) == 0


class TestCompaniesGet:
    @respx.mock
    def test_get_company(self, companies: Companies) -> None:
        respx.get(f"{BASE}/companies/760253573").mock(
            return_value=httpx.Response(
                200, content=json.dumps(COMPANY_JSON).encode()
            )
        )
        resp = companies.get(760253573)
        assert resp.parsed.id == 760253573
        assert resp.parsed.tags == ["Netzwerk", "Druckerei"]


class TestCompaniesCreate:
    @respx.mock
    def test_create_company(self, companies: Companies) -> None:
        respx.post(f"{BASE}/companies").mock(
            return_value=httpx.Response(
                200, content=json.dumps(COMPANY_JSON).encode()
            )
        )
        resp = companies.create(
            name="Beispiel AG", type="customer", currency="CHF"
        )
        assert resp.parsed.name == "Beispiel AG"


class TestCompaniesUpdate:
    @respx.mock
    def test_update_company(self, companies: Companies) -> None:
        updated = {**COMPANY_JSON, "name": "Beispiel GmbH"}
        respx.put(f"{BASE}/companies/760253573").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = companies.update(760253573, name="Beispiel GmbH")
        assert resp.parsed.name == "Beispiel GmbH"


class TestCompaniesDelete:
    @respx.mock
    def test_delete_company(self, companies: Companies) -> None:
        respx.delete(f"{BASE}/companies/760253573").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = companies.delete(760253573)
        assert resp.parsed is None


class TestCompaniesArchive:
    @respx.mock
    def test_archive_company(self, companies: Companies) -> None:
        archived = {**COMPANY_JSON, "active": False, "archived_on": "2024-01-01"}
        respx.put(f"{BASE}/companies/760253573/archive").mock(
            return_value=httpx.Response(
                200, content=json.dumps(archived).encode()
            )
        )
        resp = companies.archive(760253573)
        assert resp.parsed.active is False


class TestCompaniesUnarchive:
    @respx.mock
    def test_unarchive_company(self, companies: Companies) -> None:
        respx.put(f"{BASE}/companies/760253573/unarchive").mock(
            return_value=httpx.Response(
                200, content=json.dumps(COMPANY_JSON).encode()
            )
        )
        resp = companies.unarchive(760253573)
        assert resp.parsed.active is True
