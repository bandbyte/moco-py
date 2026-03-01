"""Tests for the Profile resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.types.profile import Profile

BASE = "https://test.mocoapp.com/api/v1"

PROFILE_JSON = {
    "id": 237852983,
    "email": "janine.kuesters@meinefirma.de",
    "full_name": "Janine Küsters",
    "first_name": "Janine",
    "last_name": "Küsters",
    "active": True,
    "external": False,
    "avatar_url": "https://data.mocoapp.com/objects/6bf3db0a.jpg",
    "unit": {
        "id": 436796,
        "name": "Design",
    },
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2022-08-02T14:21:56Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


class TestProfileGet:
    @respx.mock
    def test_get_profile(self, client: Moco) -> None:
        respx.get(f"{BASE}/profile").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PROFILE_JSON).encode()
            )
        )
        resp = client.profile.get()
        assert isinstance(resp.parsed, Profile)
        assert resp.parsed.id == 237852983
        assert resp.parsed.full_name == "Janine Küsters"
        assert resp.parsed.unit.name == "Design"
