"""Account Custom Properties resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.account_custom_properties import CustomProperty


class AccountCustomProperties(SyncResource):
    """Synchronous account custom properties resource."""

    def list(self, *, entity: str | None = None) -> SyncPage[CustomProperty]:
        """Retrieve all custom properties."""
        params: dict[str, Any] = {}
        if entity is not None:
            params["entity"] = entity
        return self._get_list(
            "/account/custom_properties", params=params, cast_to=CustomProperty
        )

    def get(self, property_id: int) -> MocoResponse[CustomProperty]:
        """Retrieve a single custom property."""
        return self._get(
            f"/account/custom_properties/{property_id}",
            cast_to=CustomProperty,
        )

    def create(
        self,
        *,
        name: str,
        kind: str,
        entity: str,
        placeholder: str | None = None,
        placeholder_alt: str | None = None,
        print_on_invoice: bool | None = None,
        print_on_offer: bool | None = None,
        print_on_timesheet: bool | None = None,
        notification_enabled: bool | None = None,
        api_only: bool | None = None,
        defaults: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[CustomProperty]:
        """Create a custom property."""
        body: dict[str, Any] = {
            "name": name,
            "kind": kind,
            "entity": entity,
        }
        if placeholder is not None:
            body["placeholder"] = placeholder
        if placeholder_alt is not None:
            body["placeholder_alt"] = placeholder_alt
        if print_on_invoice is not None:
            body["print_on_invoice"] = print_on_invoice
        if print_on_offer is not None:
            body["print_on_offer"] = print_on_offer
        if print_on_timesheet is not None:
            body["print_on_timesheet"] = print_on_timesheet
        if notification_enabled is not None:
            body["notification_enabled"] = notification_enabled
        if api_only is not None:
            body["api_only"] = api_only
        if defaults is not None:
            body["defaults"] = defaults
        return self._post(
            "/account/custom_properties",
            json_data=body,
            cast_to=CustomProperty,
        )

    def update(
        self,
        property_id: int,
        *,
        name: str | None = None,
        placeholder: str | None = None,
        placeholder_alt: str | None = None,
        print_on_invoice: bool | None = None,
        print_on_offer: bool | None = None,
        print_on_timesheet: bool | None = None,
        notification_enabled: bool | None = None,
        api_only: bool | None = None,
        defaults: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[CustomProperty]:
        """Update a custom property."""
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if placeholder is not None:
            body["placeholder"] = placeholder
        if placeholder_alt is not None:
            body["placeholder_alt"] = placeholder_alt
        if print_on_invoice is not None:
            body["print_on_invoice"] = print_on_invoice
        if print_on_offer is not None:
            body["print_on_offer"] = print_on_offer
        if print_on_timesheet is not None:
            body["print_on_timesheet"] = print_on_timesheet
        if notification_enabled is not None:
            body["notification_enabled"] = notification_enabled
        if api_only is not None:
            body["api_only"] = api_only
        if defaults is not None:
            body["defaults"] = defaults
        return self._patch(
            f"/account/custom_properties/{property_id}",
            json_data=body,
            cast_to=CustomProperty,
        )

    def delete(self, property_id: int) -> MocoResponse[None]:
        """Delete a custom property."""
        return self._delete(f"/account/custom_properties/{property_id}")


class AsyncAccountCustomProperties(AsyncResource):
    """Asynchronous account custom properties resource."""

    async def list(self, *, entity: str | None = None) -> AsyncPage[CustomProperty]:
        """Retrieve all custom properties."""
        params: dict[str, Any] = {}
        if entity is not None:
            params["entity"] = entity
        return await self._get_list(
            "/account/custom_properties", params=params, cast_to=CustomProperty
        )

    async def get(self, property_id: int) -> MocoResponse[CustomProperty]:
        """Retrieve a single custom property."""
        return await self._get(
            f"/account/custom_properties/{property_id}",
            cast_to=CustomProperty,
        )

    async def create(
        self,
        *,
        name: str,
        kind: str,
        entity: str,
        placeholder: str | None = None,
        placeholder_alt: str | None = None,
        print_on_invoice: bool | None = None,
        print_on_offer: bool | None = None,
        print_on_timesheet: bool | None = None,
        notification_enabled: bool | None = None,
        api_only: bool | None = None,
        defaults: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[CustomProperty]:
        """Create a custom property."""
        body: dict[str, Any] = {
            "name": name,
            "kind": kind,
            "entity": entity,
        }
        if placeholder is not None:
            body["placeholder"] = placeholder
        if placeholder_alt is not None:
            body["placeholder_alt"] = placeholder_alt
        if print_on_invoice is not None:
            body["print_on_invoice"] = print_on_invoice
        if print_on_offer is not None:
            body["print_on_offer"] = print_on_offer
        if print_on_timesheet is not None:
            body["print_on_timesheet"] = print_on_timesheet
        if notification_enabled is not None:
            body["notification_enabled"] = notification_enabled
        if api_only is not None:
            body["api_only"] = api_only
        if defaults is not None:
            body["defaults"] = defaults
        return await self._post(
            "/account/custom_properties",
            json_data=body,
            cast_to=CustomProperty,
        )

    async def update(
        self,
        property_id: int,
        *,
        name: str | None = None,
        placeholder: str | None = None,
        placeholder_alt: str | None = None,
        print_on_invoice: bool | None = None,
        print_on_offer: bool | None = None,
        print_on_timesheet: bool | None = None,
        notification_enabled: bool | None = None,
        api_only: bool | None = None,
        defaults: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[CustomProperty]:
        """Update a custom property."""
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if placeholder is not None:
            body["placeholder"] = placeholder
        if placeholder_alt is not None:
            body["placeholder_alt"] = placeholder_alt
        if print_on_invoice is not None:
            body["print_on_invoice"] = print_on_invoice
        if print_on_offer is not None:
            body["print_on_offer"] = print_on_offer
        if print_on_timesheet is not None:
            body["print_on_timesheet"] = print_on_timesheet
        if notification_enabled is not None:
            body["notification_enabled"] = notification_enabled
        if api_only is not None:
            body["api_only"] = api_only
        if defaults is not None:
            body["defaults"] = defaults
        return await self._patch(
            f"/account/custom_properties/{property_id}",
            json_data=body,
            cast_to=CustomProperty,
        )

    async def delete(self, property_id: int) -> MocoResponse[None]:
        """Delete a custom property."""
        return await self._delete(f"/account/custom_properties/{property_id}")
