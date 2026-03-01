"""Offers resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import OfferChangeAddress, OfferStatus
from ..types.offers import Offer


def _filter_params(
    *,
    status: OfferStatus | None = None,
    from_date: str | None = None,
    to_date: str | None = None,
    identifier: str | None = None,
    deal_id: str | None = None,
    project_id: str | None = None,
    company_id: str | None = None,
) -> dict[str, Any] | None:
    params: dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    if from_date is not None:
        params["from"] = from_date
    if to_date is not None:
        params["to"] = to_date
    if identifier is not None:
        params["identifier"] = identifier
    if deal_id is not None:
        params["deal_id"] = deal_id
    if project_id is not None:
        params["project_id"] = project_id
    if company_id is not None:
        params["company_id"] = company_id
    return params or None


class Offers(SyncResource):
    """Synchronous offers resource."""

    def list(
        self,
        *,
        status: OfferStatus | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        identifier: str | None = None,
        deal_id: str | None = None,
        project_id: str | None = None,
        company_id: str | None = None,
    ) -> SyncPage[Offer]:
        """Retrieve all offers."""
        params = _filter_params(
            status=status,
            from_date=from_date,
            to_date=to_date,
            identifier=identifier,
            deal_id=deal_id,
            project_id=project_id,
            company_id=company_id,
        )
        return self._get_list("/offers", params=params, cast_to=Offer)

    def get(self, offer_id: int) -> MocoResponse[Offer]:
        """Retrieve a single offer."""
        return self._get(f"/offers/{offer_id}", cast_to=Offer)

    def create(
        self,
        *,
        recipient_address: str,
        date: str,
        due_date: str,
        title: str,
        tax: float,
        items: list[dict[str, Any]],  # type: ignore[valid-type]
        company_id: int | None = None,
        deal_id: int | None = None,
        project_id: int | None = None,
        currency: str | None = None,
        change_address: OfferChangeAddress | None = None,
        salutation: str | None = None,
        footer: str | None = None,
        discount: float | None = None,
        contact_id: int | None = None,
        internal_contact_id: int | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        custom_properties: dict[str, str] | None = None,
        print_detail_columns: bool | None = None,
    ) -> MocoResponse[Offer]:
        """Create an offer."""
        data: dict[str, Any] = {
            "recipient_address": recipient_address,
            "date": date,
            "due_date": due_date,
            "title": title,
            "tax": tax,
            "items": items,
        }
        if company_id is not None:
            data["company_id"] = company_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        if project_id is not None:
            data["project_id"] = project_id
        if currency is not None:
            data["currency"] = currency
        if change_address is not None:
            data["change_address"] = change_address
        if salutation is not None:
            data["salutation"] = salutation
        if footer is not None:
            data["footer"] = footer
        if discount is not None:
            data["discount"] = discount
        if contact_id is not None:
            data["contact_id"] = contact_id
        if internal_contact_id is not None:
            data["internal_contact_id"] = internal_contact_id
        if tags is not None:
            data["tags"] = tags
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if print_detail_columns is not None:
            data["print_detail_columns"] = print_detail_columns
        return self._post("/offers", json_data=data, cast_to=Offer)

    def assign(
        self,
        offer_id: int,
        *,
        company_id: int | None = None,
        project_id: int | None = None,
        deal_id: int | None = None,
    ) -> MocoResponse[None]:
        """Assign an offer to a company, project, and/or deal."""
        data: dict[str, Any] = {}
        if company_id is not None:
            data["company_id"] = company_id
        if project_id is not None:
            data["project_id"] = project_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        return self._put(
            f"/offers/{offer_id}/assign",
            json_data=data,
            cast_to=None,  # type: ignore[arg-type]
        )

    def update_status(self, offer_id: int, *, status: OfferStatus) -> MocoResponse[None]:
        """Update an offer status."""
        return self._put(
            f"/offers/{offer_id}/update_status",
            json_data={"status": status},
            cast_to=None,  # type: ignore[arg-type]
        )

    def send_email(
        self,
        offer_id: int,
        *,
        subject: str,
        text: str,
        emails_to: str | None = None,
        emails_cc: str | None = None,
        emails_bcc: str | None = None,
    ) -> MocoResponse[None]:
        """Send the offer by email."""
        data: dict[str, Any] = {"subject": subject, "text": text}
        if emails_to is not None:
            data["emails_to"] = emails_to
        if emails_cc is not None:
            data["emails_cc"] = emails_cc
        if emails_bcc is not None:
            data["emails_bcc"] = emails_bcc
        return self._post(
            f"/offers/{offer_id}/send_email",
            json_data=data,
            cast_to=None,  # type: ignore[arg-type]
        )

    def list_attachments(self, offer_id: int) -> SyncPage[dict[str, Any]]:
        """List all attachments for an offer."""
        return self._get_list(
            f"/offers/{offer_id}/attachments",
            cast_to=dict,
        )

    def create_attachment(
        self,
        offer_id: int,
        *,
        filename: str,
        base64: str,
    ) -> MocoResponse[None]:
        """Add an attachment PDF to an offer."""
        return self._post(
            f"/offers/{offer_id}/attachments",
            json_data={"attachment": {"filename": filename, "base64": base64}},
            cast_to=None,  # type: ignore[arg-type]
        )

    def delete_attachment(
        self, offer_id: int, attachment_id: int
    ) -> MocoResponse[None]:
        """Remove an attachment from an offer."""
        return self._delete(f"/offers/{offer_id}/attachments/{attachment_id}")


class AsyncOffers(AsyncResource):
    """Asynchronous offers resource."""

    async def list(
        self,
        *,
        status: OfferStatus | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        identifier: str | None = None,
        deal_id: str | None = None,
        project_id: str | None = None,
        company_id: str | None = None,
    ) -> AsyncPage[Offer]:
        """Retrieve all offers."""
        params = _filter_params(
            status=status,
            from_date=from_date,
            to_date=to_date,
            identifier=identifier,
            deal_id=deal_id,
            project_id=project_id,
            company_id=company_id,
        )
        return await self._get_list("/offers", params=params, cast_to=Offer)

    async def get(self, offer_id: int) -> MocoResponse[Offer]:
        """Retrieve a single offer."""
        return await self._get(f"/offers/{offer_id}", cast_to=Offer)

    async def create(
        self,
        *,
        recipient_address: str,
        date: str,
        due_date: str,
        title: str,
        tax: float,
        items: list[dict[str, Any]],  # type: ignore[valid-type]
        company_id: int | None = None,
        deal_id: int | None = None,
        project_id: int | None = None,
        currency: str | None = None,
        change_address: OfferChangeAddress | None = None,
        salutation: str | None = None,
        footer: str | None = None,
        discount: float | None = None,
        contact_id: int | None = None,
        internal_contact_id: int | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        custom_properties: dict[str, str] | None = None,
        print_detail_columns: bool | None = None,
    ) -> MocoResponse[Offer]:
        """Create an offer."""
        data: dict[str, Any] = {
            "recipient_address": recipient_address,
            "date": date,
            "due_date": due_date,
            "title": title,
            "tax": tax,
            "items": items,
        }
        if company_id is not None:
            data["company_id"] = company_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        if project_id is not None:
            data["project_id"] = project_id
        if currency is not None:
            data["currency"] = currency
        if change_address is not None:
            data["change_address"] = change_address
        if salutation is not None:
            data["salutation"] = salutation
        if footer is not None:
            data["footer"] = footer
        if discount is not None:
            data["discount"] = discount
        if contact_id is not None:
            data["contact_id"] = contact_id
        if internal_contact_id is not None:
            data["internal_contact_id"] = internal_contact_id
        if tags is not None:
            data["tags"] = tags
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if print_detail_columns is not None:
            data["print_detail_columns"] = print_detail_columns
        return await self._post("/offers", json_data=data, cast_to=Offer)

    async def assign(
        self,
        offer_id: int,
        *,
        company_id: int | None = None,
        project_id: int | None = None,
        deal_id: int | None = None,
    ) -> MocoResponse[None]:
        """Assign an offer to a company, project, and/or deal."""
        data: dict[str, Any] = {}
        if company_id is not None:
            data["company_id"] = company_id
        if project_id is not None:
            data["project_id"] = project_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        return await self._put(
            f"/offers/{offer_id}/assign",
            json_data=data,
            cast_to=None,  # type: ignore[arg-type]
        )

    async def update_status(self, offer_id: int, *, status: OfferStatus) -> MocoResponse[None]:
        """Update an offer status."""
        return await self._put(
            f"/offers/{offer_id}/update_status",
            json_data={"status": status},
            cast_to=None,  # type: ignore[arg-type]
        )

    async def send_email(
        self,
        offer_id: int,
        *,
        subject: str,
        text: str,
        emails_to: str | None = None,
        emails_cc: str | None = None,
        emails_bcc: str | None = None,
    ) -> MocoResponse[None]:
        """Send the offer by email."""
        data: dict[str, Any] = {"subject": subject, "text": text}
        if emails_to is not None:
            data["emails_to"] = emails_to
        if emails_cc is not None:
            data["emails_cc"] = emails_cc
        if emails_bcc is not None:
            data["emails_bcc"] = emails_bcc
        return await self._post(
            f"/offers/{offer_id}/send_email",
            json_data=data,
            cast_to=None,  # type: ignore[arg-type]
        )

    async def list_attachments(self, offer_id: int) -> AsyncPage[dict[str, Any]]:
        """List all attachments for an offer."""
        return await self._get_list(
            f"/offers/{offer_id}/attachments",
            cast_to=dict,
        )

    async def create_attachment(
        self,
        offer_id: int,
        *,
        filename: str,
        base64: str,
    ) -> MocoResponse[None]:
        """Add an attachment PDF to an offer."""
        return await self._post(
            f"/offers/{offer_id}/attachments",
            json_data={"attachment": {"filename": filename, "base64": base64}},
            cast_to=None,  # type: ignore[arg-type]
        )

    async def delete_attachment(
        self, offer_id: int, attachment_id: int
    ) -> MocoResponse[None]:
        """Remove an attachment from an offer."""
        return await self._delete(f"/offers/{offer_id}/attachments/{attachment_id}")
