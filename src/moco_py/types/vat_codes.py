"""Pydantic models for the VAT Codes resource."""

from __future__ import annotations

from pydantic import BaseModel


class VatCodeSale(BaseModel):
    """A sale VAT code in MOCO."""

    id: int
    tax: float
    reverse_charge: bool
    intra_eu: bool
    active: bool
    print_gross_total: bool
    notice_tax_exemption: str
    notice_tax_exemption_alt: str
    code: str
    credit_account: str | None = None


class VatCodePurchase(BaseModel):
    """A purchase VAT code in MOCO."""

    id: int
    tax: float
    reverse_charge: bool
    intra_eu: bool
    active: bool
    code: str
