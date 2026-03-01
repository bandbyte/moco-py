"""Offer Customer Approval resource."""

from __future__ import annotations

from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.offer_customer_approval import OfferCustomerApproval


class OfferCustomerApprovals(SyncResource):
    """Synchronous offer customer approval resource."""

    def get(self, offer_id: int) -> MocoResponse[OfferCustomerApproval]:
        """Retrieve the customer approval for an offer."""
        return self._get(
            f"/offers/{offer_id}/customer_approval",
            cast_to=OfferCustomerApproval,
        )

    def activate(self, offer_id: int) -> MocoResponse[OfferCustomerApproval]:
        """Activate a customer approval for an offer."""
        return self._post(
            f"/offers/{offer_id}/customer_approval/activate",
            json_data={},
            cast_to=OfferCustomerApproval,
        )

    def deactivate(self, offer_id: int) -> MocoResponse[OfferCustomerApproval]:
        """Deactivate a customer approval for an offer."""
        return self._post(
            f"/offers/{offer_id}/customer_approval/deactivate",
            json_data={},
            cast_to=OfferCustomerApproval,
        )


class AsyncOfferCustomerApprovals(AsyncResource):
    """Asynchronous offer customer approval resource."""

    async def get(self, offer_id: int) -> MocoResponse[OfferCustomerApproval]:
        """Retrieve the customer approval for an offer."""
        return await self._get(
            f"/offers/{offer_id}/customer_approval",
            cast_to=OfferCustomerApproval,
        )

    async def activate(self, offer_id: int) -> MocoResponse[OfferCustomerApproval]:
        """Activate a customer approval for an offer."""
        return await self._post(
            f"/offers/{offer_id}/customer_approval/activate",
            json_data={},
            cast_to=OfferCustomerApproval,
        )

    async def deactivate(self, offer_id: int) -> MocoResponse[OfferCustomerApproval]:
        """Deactivate a customer approval for an offer."""
        return await self._post(
            f"/offers/{offer_id}/customer_approval/deactivate",
            json_data={},
            cast_to=OfferCustomerApproval,
        )
