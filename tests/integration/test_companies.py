"""Integration tests for the Companies resource."""

from __future__ import annotations

import pytest

from moco_py import Moco
from moco_py.types._enums import CompanyType
from moco_py.types.companies import Company

pytestmark = pytest.mark.integration


class TestCompaniesList:
    def test_list_returns_companies(self, moco_client: Moco) -> None:
        page = moco_client.companies.list()
        assert isinstance(page.items, list)
        if page.items:
            assert isinstance(page.items[0], Company)


class TestCompaniesGet:
    def test_get_single_company(self, moco_client: Moco) -> None:
        page = moco_client.companies.list()
        if not page.items:
            pytest.skip("No companies in test environment")
        response = moco_client.companies.get(page.items[0].id)
        assert isinstance(response.parsed, Company)
        assert response.parsed.id == page.items[0].id


class TestCompaniesMutations:
    def test_create_get_update_delete(self, moco_client: Moco) -> None:
        # Create
        created = moco_client.companies.create(
            name="__moco_py_test__company_crud",
            type=CompanyType.CUSTOMER,
        ).parsed
        try:
            assert isinstance(created, Company)
            assert created.name == "__moco_py_test__company_crud"

            # Get
            fetched = moco_client.companies.get(created.id).parsed
            assert fetched.id == created.id

            # Update
            updated = moco_client.companies.update(
                created.id, name="__moco_py_test__company_updated"
            ).parsed
            assert updated.name == "__moco_py_test__company_updated"
        finally:
            # Delete
            moco_client.companies.delete(created.id)
