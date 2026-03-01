"""Integration tests for the Comments resource."""

from __future__ import annotations

import pytest

from moco_py import Moco
from moco_py.types._enums import CommentableType
from moco_py.types.comments import Comment

pytestmark = pytest.mark.integration


class TestCommentsMutations:
    def test_create_update_delete(self, moco_client: Moco, temp_company: int) -> None:
        created = moco_client.comments.create(
            commentable_id=temp_company,
            commentable_type=CommentableType.COMPANY,
            text="__moco_py_test__comment",
        ).parsed
        try:
            assert isinstance(created, Comment)
            assert created.text == "__moco_py_test__comment"

            updated = moco_client.comments.update(
                created.id, text="__moco_py_test__comment_updated"
            ).parsed
            assert updated.text == "__moco_py_test__comment_updated"
        finally:
            moco_client.comments.delete(created.id)
