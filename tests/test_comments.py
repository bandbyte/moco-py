"""Tests for the Comments resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.comments import Comments
from moco_py.types.comments import Comment

BASE = "https://test.mocoapp.com/api/v1"

COMMENT_JSON = {
    "id": 123,
    "commentable_id": 12345,
    "commentable_type": "Project",
    "text": "<div>Project was ordered on <strong>1.10.2017</strong></div>.",
    "manual": True,
    "user": {"id": 567, "firstname": "Tobias", "lastname": "Miesel"},
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def comments(client: Moco) -> Comments:
    return Comments(client._transport)


class TestCommentsList:
    @respx.mock
    def test_list_comments(self, comments: Comments) -> None:
        respx.get(f"{BASE}/comments").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([COMMENT_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = comments.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Comment)
        assert page.items[0].commentable_type == "Project"

    @respx.mock
    def test_list_comments_with_filters(self, comments: Comments) -> None:
        respx.get(f"{BASE}/comments").mock(
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
        page = comments.list(
            commentable_type="Project", commentable_id=12345
        )
        assert len(page.items) == 0


class TestCommentsGet:
    @respx.mock
    def test_get_comment(self, comments: Comments) -> None:
        respx.get(f"{BASE}/comments/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(COMMENT_JSON).encode()
            )
        )
        resp = comments.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.user.firstname == "Tobias"


class TestCommentsCreate:
    @respx.mock
    def test_create_comment(self, comments: Comments) -> None:
        respx.post(f"{BASE}/comments").mock(
            return_value=httpx.Response(
                200, content=json.dumps(COMMENT_JSON).encode()
            )
        )
        resp = comments.create(
            commentable_id=12345,
            commentable_type="Project",
            text="<div>Project was ordered on <strong>1.10.2017</strong></div>.",
        )
        assert resp.parsed.id == 123


class TestCommentsBulkCreate:
    @respx.mock
    def test_bulk_create_comments(self, comments: Comments) -> None:
        respx.post(f"{BASE}/comments/bulk").mock(
            return_value=httpx.Response(
                200, content=json.dumps([COMMENT_JSON]).encode()
            )
        )
        resp = comments.bulk_create(
            commentable_ids=[123, 234],
            commentable_type="Contact",
            text="Sent Newsletter",
        )
        assert resp.parsed[0].id == 123


class TestCommentsUpdate:
    @respx.mock
    def test_update_comment(self, comments: Comments) -> None:
        updated = {**COMMENT_JSON, "text": "Updated text"}
        respx.put(f"{BASE}/comments/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = comments.update(123, text="Updated text")
        assert resp.parsed.text == "Updated text"


class TestCommentsDelete:
    @respx.mock
    def test_delete_comment(self, comments: Comments) -> None:
        respx.delete(f"{BASE}/comments/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = comments.delete(123)
        assert resp.parsed is None
