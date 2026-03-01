"""Tests for the Account Custom Properties resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.account_custom_properties import AccountCustomProperties
from moco_py.types.account_custom_properties import CustomProperty

BASE = "https://test.mocoapp.com/api/v1"

PROPERTY_JSON = {
    "id": 8601,
    "name": "Purchase Order Number",
    "name_alt": "Numero Identificativo Acquisto",
    "placeholder": "",
    "placeholder_alt": "",
    "entity": "Project",
    "kind": "String",
    "print_on_invoice": True,
    "print_on_offer": False,
    "print_on_timesheet": True,
    "notification_enabled": False,
    "defaults": [],
    "created_at": "2022-08-15T15:31:22Z",
    "updated_at": "2022-08-15T15:31:28Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def custom_properties(client: Moco) -> AccountCustomProperties:
    return AccountCustomProperties(client._transport)


class TestCustomPropertiesList:
    @respx.mock
    def test_list_properties(self, custom_properties: AccountCustomProperties) -> None:
        respx.get(f"{BASE}/account/custom_properties").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([PROPERTY_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = custom_properties.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], CustomProperty)
        assert page.items[0].name == "Purchase Order Number"

    @respx.mock
    def test_list_properties_with_entity_filter(
        self, custom_properties: AccountCustomProperties
    ) -> None:
        respx.get(f"{BASE}/account/custom_properties").mock(
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
        page = custom_properties.list(entity="Project")
        assert len(page.items) == 0


class TestCustomPropertiesGet:
    @respx.mock
    def test_get_property(self, custom_properties: AccountCustomProperties) -> None:
        respx.get(f"{BASE}/account/custom_properties/8601").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PROPERTY_JSON).encode()
            )
        )
        resp = custom_properties.get(8601)
        assert resp.parsed.id == 8601
        assert resp.parsed.kind == "String"


class TestCustomPropertiesCreate:
    @respx.mock
    def test_create_property(self, custom_properties: AccountCustomProperties) -> None:
        respx.post(f"{BASE}/account/custom_properties").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PROPERTY_JSON).encode()
            )
        )
        resp = custom_properties.create(
            name="Purchase Order Number", kind="String", entity="Project"
        )
        assert resp.parsed.name == "Purchase Order Number"


class TestCustomPropertiesUpdate:
    @respx.mock
    def test_update_property(self, custom_properties: AccountCustomProperties) -> None:
        updated = {**PROPERTY_JSON, "name": "PO Number"}
        respx.patch(f"{BASE}/account/custom_properties/8601").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = custom_properties.update(8601, name="PO Number")
        assert resp.parsed.name == "PO Number"


class TestCustomPropertiesDelete:
    @respx.mock
    def test_delete_property(self, custom_properties: AccountCustomProperties) -> None:
        respx.delete(f"{BASE}/account/custom_properties/8601").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = custom_properties.delete(8601)
        assert resp.parsed is None
