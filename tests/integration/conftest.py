"""Shared fixtures for integration tests against a live MOCO instance."""

from __future__ import annotations

import os
from collections.abc import Generator

import pytest

from moco_py import Moco
from moco_py.types._enums import CompanyType, Gender

_api_key = os.environ.get("MOCO_API_KEY")
_domain = os.environ.get("MOCO_DOMAIN")
_missing = not _api_key or not _domain

_PREFIX = "__moco_py_test__"


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Skip all integration tests when credentials are not available."""
    if not _missing:
        return
    skip = pytest.mark.skip(reason="MOCO_API_KEY and MOCO_DOMAIN env vars required")
    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip)


@pytest.fixture(scope="session")
def moco_client() -> Generator[Moco]:
    """Session-scoped sync client reused across all integration tests."""
    assert _api_key and _domain  # guarded by skip marker above
    with Moco(api_key=_api_key, domain=_domain) as client:
        yield client


@pytest.fixture(scope="session")
def current_user_id(moco_client: Moco) -> int:
    """ID of the API key owner — needed as leader_id, user_id, etc."""
    return moco_client.users.list().items[0].id


@pytest.fixture()
def temp_company(moco_client: Moco) -> Generator[int]:
    """Create a throwaway company and delete it after the test."""
    resp = moco_client.companies.create(name=f"{_PREFIX}company", type=CompanyType.CUSTOMER)
    company_id = resp.parsed.id
    yield company_id
    moco_client.companies.delete(company_id)


@pytest.fixture()
def temp_contact(moco_client: Moco) -> Generator[int]:
    """Create a throwaway contact and delete it after the test."""
    resp = moco_client.contacts.create(lastname=f"{_PREFIX}contact", gender=Gender.MALE)
    contact_id = resp.parsed.id
    yield contact_id
    moco_client.contacts.delete(contact_id)
