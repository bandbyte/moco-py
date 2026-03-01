"""Tags resource."""

from __future__ import annotations

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.tags import Tag


class Tags(SyncResource):
    """Synchronous tags resource."""

    def list(
        self,
        *,
        context: str | None = None,
    ) -> SyncPage[Tag]:
        """Retrieve all tags."""
        params: dict[str, str] = {}
        if context is not None:
            params["context"] = context
        return self._get_list("/tags", params=params or None, cast_to=Tag)

    def get(self, tag_id: int) -> MocoResponse[Tag]:
        """Retrieve a single tag."""
        return self._get(f"/tags/{tag_id}", cast_to=Tag)

    def create(
        self,
        *,
        name: str,
        context: str,
        color: str | None = None,
    ) -> MocoResponse[Tag]:
        """Create a tag."""
        body: dict[str, str] = {"name": name, "context": context}
        if color is not None:
            body["color"] = color
        return self._post("/tags", json_data=body, cast_to=Tag)

    def update(
        self,
        tag_id: int,
        *,
        name: str | None = None,
        color: str | None = None,
    ) -> MocoResponse[Tag]:
        """Update a tag."""
        body: dict[str, str] = {}
        if name is not None:
            body["name"] = name
        if color is not None:
            body["color"] = color
        return self._put(f"/tags/{tag_id}", json_data=body, cast_to=Tag)

    def delete(self, tag_id: int) -> MocoResponse[None]:
        """Delete a tag."""
        return self._delete(f"/tags/{tag_id}")


class AsyncTags(AsyncResource):
    """Asynchronous tags resource."""

    async def list(
        self,
        *,
        context: str | None = None,
    ) -> AsyncPage[Tag]:
        """Retrieve all tags."""
        params: dict[str, str] = {}
        if context is not None:
            params["context"] = context
        return await self._get_list("/tags", params=params or None, cast_to=Tag)

    async def get(self, tag_id: int) -> MocoResponse[Tag]:
        """Retrieve a single tag."""
        return await self._get(f"/tags/{tag_id}", cast_to=Tag)

    async def create(
        self,
        *,
        name: str,
        context: str,
        color: str | None = None,
    ) -> MocoResponse[Tag]:
        """Create a tag."""
        body: dict[str, str] = {"name": name, "context": context}
        if color is not None:
            body["color"] = color
        return await self._post("/tags", json_data=body, cast_to=Tag)

    async def update(
        self,
        tag_id: int,
        *,
        name: str | None = None,
        color: str | None = None,
    ) -> MocoResponse[Tag]:
        """Update a tag."""
        body: dict[str, str] = {}
        if name is not None:
            body["name"] = name
        if color is not None:
            body["color"] = color
        return await self._put(f"/tags/{tag_id}", json_data=body, cast_to=Tag)

    async def delete(self, tag_id: int) -> MocoResponse[None]:
        """Delete a tag."""
        return await self._delete(f"/tags/{tag_id}")
