"""Units (Teams) resource."""

from __future__ import annotations

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.units import Unit


class Units(SyncResource):
    """Synchronous units resource."""

    def list(self) -> SyncPage[Unit]:
        """Retrieve all units."""
        return self._get_list("/units", cast_to=Unit)

    def get(self, unit_id: int) -> MocoResponse[Unit]:
        """Retrieve a single unit."""
        return self._get(f"/units/{unit_id}", cast_to=Unit)

    def create(self, *, name: str) -> MocoResponse[Unit]:
        """Create a unit."""
        return self._post("/units", json_data={"name": name}, cast_to=Unit)

    def update(self, unit_id: int, *, name: str) -> MocoResponse[Unit]:
        """Update a unit."""
        return self._put(
            f"/units/{unit_id}",
            json_data={"name": name},
            cast_to=Unit,
        )

    def delete(self, unit_id: int) -> MocoResponse[None]:
        """Delete a unit."""
        return self._delete(f"/units/{unit_id}")


class AsyncUnits(AsyncResource):
    """Asynchronous units resource."""

    async def list(self) -> AsyncPage[Unit]:
        """Retrieve all units."""
        return await self._get_list("/units", cast_to=Unit)

    async def get(self, unit_id: int) -> MocoResponse[Unit]:
        """Retrieve a single unit."""
        return await self._get(f"/units/{unit_id}", cast_to=Unit)

    async def create(self, *, name: str) -> MocoResponse[Unit]:
        """Create a unit."""
        return await self._post("/units", json_data={"name": name}, cast_to=Unit)

    async def update(self, unit_id: int, *, name: str) -> MocoResponse[Unit]:
        """Update a unit."""
        return await self._put(
            f"/units/{unit_id}",
            json_data={"name": name},
            cast_to=Unit,
        )

    async def delete(self, unit_id: int) -> MocoResponse[None]:
        """Delete a unit."""
        return await self._delete(f"/units/{unit_id}")
