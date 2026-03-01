"""Comments resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import CommentableType
from ..types.comments import Comment


class Comments(SyncResource):
    """Synchronous comments resource."""

    def list(
        self,
        *,
        commentable_type: CommentableType | None = None,
        commentable_id: int | None = None,
        user_id: int | None = None,
        manual: bool | None = None,
    ) -> SyncPage[Comment]:
        """Retrieve all comments."""
        params: dict[str, Any] = {}
        if commentable_type is not None:
            params["commentable_type"] = commentable_type
        if commentable_id is not None:
            params["commentable_id"] = commentable_id
        if user_id is not None:
            params["user_id"] = user_id
        if manual is not None:
            params["manual"] = manual
        return self._get_list("/comments", params=params, cast_to=Comment)

    def get(self, comment_id: int) -> MocoResponse[Comment]:
        """Retrieve a single comment."""
        return self._get(f"/comments/{comment_id}", cast_to=Comment)

    def create(
        self,
        *,
        commentable_id: int,
        commentable_type: CommentableType,
        text: str,
        attachment_filename: str | None = None,
        attachment_content: str | None = None,
    ) -> MocoResponse[Comment]:
        """Create a comment."""
        data: dict[str, Any] = {
            "commentable_id": commentable_id,
            "commentable_type": commentable_type,
            "text": text,
        }
        if attachment_filename is not None:
            data["attachment_filename"] = attachment_filename
        if attachment_content is not None:
            data["attachment_content"] = attachment_content
        return self._post("/comments", json_data=data, cast_to=Comment)

    def bulk_create(
        self,
        *,
        commentable_ids: list[int],  # type: ignore[valid-type]
        commentable_type: CommentableType,
        text: str,
    ) -> MocoResponse[list[Comment]]:  # type: ignore[valid-type]
        """Create multiple comments in bulk."""
        data: dict[str, Any] = {
            "commentable_ids": commentable_ids,
            "commentable_type": commentable_type,
            "text": text,
        }
        return self._transport.request(
            "POST",
            "/comments/bulk",
            json_data=data,
            cast_to=Comment,
            is_list=True,
        )

    def update(
        self,
        comment_id: int,
        *,
        text: str,
    ) -> MocoResponse[Comment]:
        """Update a comment."""
        return self._put(
            f"/comments/{comment_id}",
            json_data={"text": text},
            cast_to=Comment,
        )

    def delete(self, comment_id: int) -> MocoResponse[None]:
        """Delete a comment."""
        return self._delete(f"/comments/{comment_id}")


class AsyncComments(AsyncResource):
    """Asynchronous comments resource."""

    async def list(
        self,
        *,
        commentable_type: CommentableType | None = None,
        commentable_id: int | None = None,
        user_id: int | None = None,
        manual: bool | None = None,
    ) -> AsyncPage[Comment]:
        """Retrieve all comments."""
        params: dict[str, Any] = {}
        if commentable_type is not None:
            params["commentable_type"] = commentable_type
        if commentable_id is not None:
            params["commentable_id"] = commentable_id
        if user_id is not None:
            params["user_id"] = user_id
        if manual is not None:
            params["manual"] = manual
        return await self._get_list("/comments", params=params, cast_to=Comment)

    async def get(self, comment_id: int) -> MocoResponse[Comment]:
        """Retrieve a single comment."""
        return await self._get(f"/comments/{comment_id}", cast_to=Comment)

    async def create(
        self,
        *,
        commentable_id: int,
        commentable_type: CommentableType,
        text: str,
        attachment_filename: str | None = None,
        attachment_content: str | None = None,
    ) -> MocoResponse[Comment]:
        """Create a comment."""
        data: dict[str, Any] = {
            "commentable_id": commentable_id,
            "commentable_type": commentable_type,
            "text": text,
        }
        if attachment_filename is not None:
            data["attachment_filename"] = attachment_filename
        if attachment_content is not None:
            data["attachment_content"] = attachment_content
        return await self._post("/comments", json_data=data, cast_to=Comment)

    async def bulk_create(
        self,
        *,
        commentable_ids: list[int],  # type: ignore[valid-type]
        commentable_type: CommentableType,
        text: str,
    ) -> MocoResponse[list[Comment]]:  # type: ignore[valid-type]
        """Create multiple comments in bulk."""
        data: dict[str, Any] = {
            "commentable_ids": commentable_ids,
            "commentable_type": commentable_type,
            "text": text,
        }
        return await self._transport.request(
            "POST",
            "/comments/bulk",
            json_data=data,
            cast_to=Comment,
            is_list=True,
        )

    async def update(
        self,
        comment_id: int,
        *,
        text: str,
    ) -> MocoResponse[Comment]:
        """Update a comment."""
        return await self._put(
            f"/comments/{comment_id}",
            json_data={"text": text},
            cast_to=Comment,
        )

    async def delete(self, comment_id: int) -> MocoResponse[None]:
        """Delete a comment."""
        return await self._delete(f"/comments/{comment_id}")
