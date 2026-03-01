"""Companies resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import CompanyType
from ..types.companies import Company


class Companies(SyncResource):
    """Synchronous companies resource."""

    def list(
        self,
        *,
        include_archived: bool | None = None,
        type: CompanyType | None = None,
        tags: str | None = None,
        identifier: str | None = None,
        term: str | None = None,
    ) -> SyncPage[Company]:
        """Retrieve all companies."""
        params: dict[str, Any] = {}
        if include_archived is not None:
            params["include_archived"] = include_archived
        if type is not None:
            params["type"] = type
        if tags is not None:
            params["tags"] = tags
        if identifier is not None:
            params["identifier"] = identifier
        if term is not None:
            params["term"] = term
        return self._get_list("/companies", params=params, cast_to=Company)

    def get(self, company_id: int) -> MocoResponse[Company]:
        """Retrieve a single company."""
        return self._get(f"/companies/{company_id}", cast_to=Company)

    def create(
        self,
        *,
        name: str,
        type: CompanyType,
        currency: str | None = None,
        identifier: str | None = None,
        country_code: str | None = None,
        vat_identifier: str | None = None,
        website: str | None = None,
        fax: str | None = None,
        phone: str | None = None,
        email: str | None = None,
        billing_email_cc: str | None = None,
        billing_notes: str | None = None,
        address: str | None = None,
        info: str | None = None,
        custom_properties: dict[str, Any] | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        user_id: int | None = None,
        footer: str | None = None,
        customer_tax: float | None = None,
        supplier_tax: float | None = None,
        default_invoice_due_days: int | None = None,
        debit_number: int | None = None,
        credit_number: int | None = None,
    ) -> MocoResponse[Company]:
        """Create a company."""
        data: dict[str, Any] = {"name": name, "type": type}
        for key, value in {
            "currency": currency,
            "identifier": identifier,
            "country_code": country_code,
            "vat_identifier": vat_identifier,
            "website": website,
            "fax": fax,
            "phone": phone,
            "email": email,
            "billing_email_cc": billing_email_cc,
            "billing_notes": billing_notes,
            "address": address,
            "info": info,
            "custom_properties": custom_properties,
            "tags": tags,
            "user_id": user_id,
            "footer": footer,
            "customer_tax": customer_tax,
            "supplier_tax": supplier_tax,
            "default_invoice_due_days": default_invoice_due_days,
            "debit_number": debit_number,
            "credit_number": credit_number,
        }.items():
            if value is not None:
                data[key] = value
        return self._post("/companies", json_data=data, cast_to=Company)

    def update(
        self,
        company_id: int,
        *,
        name: str | None = None,
        type: CompanyType | None = None,
        currency: str | None = None,
        identifier: str | None = None,
        country_code: str | None = None,
        vat_identifier: str | None = None,
        website: str | None = None,
        fax: str | None = None,
        phone: str | None = None,
        email: str | None = None,
        billing_email_cc: str | None = None,
        billing_notes: str | None = None,
        address: str | None = None,
        info: str | None = None,
        custom_properties: dict[str, Any] | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        user_id: int | None = None,
        footer: str | None = None,
        customer_tax: float | None = None,
        supplier_tax: float | None = None,
        default_invoice_due_days: int | None = None,
        debit_number: int | None = None,
        credit_number: int | None = None,
    ) -> MocoResponse[Company]:
        """Update a company."""
        data: dict[str, Any] = {}
        for key, value in {
            "name": name,
            "type": type,
            "currency": currency,
            "identifier": identifier,
            "country_code": country_code,
            "vat_identifier": vat_identifier,
            "website": website,
            "fax": fax,
            "phone": phone,
            "email": email,
            "billing_email_cc": billing_email_cc,
            "billing_notes": billing_notes,
            "address": address,
            "info": info,
            "custom_properties": custom_properties,
            "tags": tags,
            "user_id": user_id,
            "footer": footer,
            "customer_tax": customer_tax,
            "supplier_tax": supplier_tax,
            "default_invoice_due_days": default_invoice_due_days,
            "debit_number": debit_number,
            "credit_number": credit_number,
        }.items():
            if value is not None:
                data[key] = value
        return self._put(f"/companies/{company_id}", json_data=data, cast_to=Company)

    def delete(self, company_id: int) -> MocoResponse[None]:
        """Delete a company."""
        return self._delete(f"/companies/{company_id}")

    def archive(self, company_id: int) -> MocoResponse[Company]:
        """Archive a company."""
        return self._put(f"/companies/{company_id}/archive", cast_to=Company)

    def unarchive(self, company_id: int) -> MocoResponse[Company]:
        """Unarchive a company."""
        return self._put(f"/companies/{company_id}/unarchive", cast_to=Company)


class AsyncCompanies(AsyncResource):
    """Asynchronous companies resource."""

    async def list(
        self,
        *,
        include_archived: bool | None = None,
        type: CompanyType | None = None,
        tags: str | None = None,
        identifier: str | None = None,
        term: str | None = None,
    ) -> AsyncPage[Company]:
        """Retrieve all companies."""
        params: dict[str, Any] = {}
        if include_archived is not None:
            params["include_archived"] = include_archived
        if type is not None:
            params["type"] = type
        if tags is not None:
            params["tags"] = tags
        if identifier is not None:
            params["identifier"] = identifier
        if term is not None:
            params["term"] = term
        return await self._get_list("/companies", params=params, cast_to=Company)

    async def get(self, company_id: int) -> MocoResponse[Company]:
        """Retrieve a single company."""
        return await self._get(f"/companies/{company_id}", cast_to=Company)

    async def create(
        self,
        *,
        name: str,
        type: CompanyType,
        currency: str | None = None,
        identifier: str | None = None,
        country_code: str | None = None,
        vat_identifier: str | None = None,
        website: str | None = None,
        fax: str | None = None,
        phone: str | None = None,
        email: str | None = None,
        billing_email_cc: str | None = None,
        billing_notes: str | None = None,
        address: str | None = None,
        info: str | None = None,
        custom_properties: dict[str, Any] | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        user_id: int | None = None,
        footer: str | None = None,
        customer_tax: float | None = None,
        supplier_tax: float | None = None,
        default_invoice_due_days: int | None = None,
        debit_number: int | None = None,
        credit_number: int | None = None,
    ) -> MocoResponse[Company]:
        """Create a company."""
        data: dict[str, Any] = {"name": name, "type": type}
        for key, value in {
            "currency": currency,
            "identifier": identifier,
            "country_code": country_code,
            "vat_identifier": vat_identifier,
            "website": website,
            "fax": fax,
            "phone": phone,
            "email": email,
            "billing_email_cc": billing_email_cc,
            "billing_notes": billing_notes,
            "address": address,
            "info": info,
            "custom_properties": custom_properties,
            "tags": tags,
            "user_id": user_id,
            "footer": footer,
            "customer_tax": customer_tax,
            "supplier_tax": supplier_tax,
            "default_invoice_due_days": default_invoice_due_days,
            "debit_number": debit_number,
            "credit_number": credit_number,
        }.items():
            if value is not None:
                data[key] = value
        return await self._post("/companies", json_data=data, cast_to=Company)

    async def update(
        self,
        company_id: int,
        *,
        name: str | None = None,
        type: CompanyType | None = None,
        currency: str | None = None,
        identifier: str | None = None,
        country_code: str | None = None,
        vat_identifier: str | None = None,
        website: str | None = None,
        fax: str | None = None,
        phone: str | None = None,
        email: str | None = None,
        billing_email_cc: str | None = None,
        billing_notes: str | None = None,
        address: str | None = None,
        info: str | None = None,
        custom_properties: dict[str, Any] | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        user_id: int | None = None,
        footer: str | None = None,
        customer_tax: float | None = None,
        supplier_tax: float | None = None,
        default_invoice_due_days: int | None = None,
        debit_number: int | None = None,
        credit_number: int | None = None,
    ) -> MocoResponse[Company]:
        """Update a company."""
        data: dict[str, Any] = {}
        for key, value in {
            "name": name,
            "type": type,
            "currency": currency,
            "identifier": identifier,
            "country_code": country_code,
            "vat_identifier": vat_identifier,
            "website": website,
            "fax": fax,
            "phone": phone,
            "email": email,
            "billing_email_cc": billing_email_cc,
            "billing_notes": billing_notes,
            "address": address,
            "info": info,
            "custom_properties": custom_properties,
            "tags": tags,
            "user_id": user_id,
            "footer": footer,
            "customer_tax": customer_tax,
            "supplier_tax": supplier_tax,
            "default_invoice_due_days": default_invoice_due_days,
            "debit_number": debit_number,
            "credit_number": credit_number,
        }.items():
            if value is not None:
                data[key] = value
        return await self._put(
            f"/companies/{company_id}", json_data=data, cast_to=Company
        )

    async def delete(self, company_id: int) -> MocoResponse[None]:
        """Delete a company."""
        return await self._delete(f"/companies/{company_id}")

    async def archive(self, company_id: int) -> MocoResponse[Company]:
        """Archive a company."""
        return await self._put(f"/companies/{company_id}/archive", cast_to=Company)

    async def unarchive(self, company_id: int) -> MocoResponse[Company]:
        """Unarchive a company."""
        return await self._put(f"/companies/{company_id}/unarchive", cast_to=Company)
