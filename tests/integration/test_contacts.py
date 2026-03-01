"""Integration tests for the Contacts resource."""

from __future__ import annotations

import pytest

from moco_py import Moco
from moco_py.types._enums import Gender
from moco_py.types.contacts import Contact

pytestmark = pytest.mark.integration


class TestContactsList:
    def test_list_returns_contacts(self, moco_client: Moco) -> None:
        page = moco_client.contacts.list()
        assert isinstance(page.items, list)


class TestContactsMutations:
    def test_create_get_update_delete(self, moco_client: Moco) -> None:
        created = moco_client.contacts.create(
            lastname="__moco_py_test__contact",
            gender=Gender.MALE,
            firstname="Test",
        ).parsed
        try:
            assert isinstance(created, Contact)
            assert created.lastname == "__moco_py_test__contact"

            fetched = moco_client.contacts.get(created.id).parsed
            assert fetched.id == created.id

            updated = moco_client.contacts.update(
                created.id, lastname="__moco_py_test__contact_updated"
            ).parsed
            assert updated.lastname == "__moco_py_test__contact_updated"
        finally:
            moco_client.contacts.delete(created.id)
