"""Enum types for the MOCO API."""

from __future__ import annotations

from enum import Enum, IntEnum


class _StrEnum(str, Enum):
    """String enum compatible with Python 3.10+."""


# ── Shared / Cross-resource ─────────────────────────────────────────────


class VatType(_StrEnum):
    """VAT type used across invoices, offers, companies, and purchases."""

    TAX = "tax"
    REVERSE_CHARGE = "reverse_charge"
    INTRA_EU = "intra_eu"


class ItemType(_StrEnum):
    """Line item type for invoices and offers."""

    TITLE = "title"
    DESCRIPTION = "description"
    ITEM = "item"
    SUBTOTAL = "subtotal"
    PAGE_BREAK = "page-break"
    SEPARATOR = "separator"


class SubtotalType(_StrEnum):
    """Subtotal variant (when item type is 'subtotal')."""

    PART_TOTAL = "part_total"
    SUB_TOTAL = "sub_total"


class OfferSubtotalType(_StrEnum):
    """Subtotal variant for offers (extends SubtotalType with optional variants)."""

    PART_TOTAL = "part_total"
    SUB_TOTAL = "sub_total"
    OPTIONAL_PART_TOTAL = "optional_part_total"
    OPTIONAL_SUB_TOTAL = "optional_sub_total"


class ServiceType(_StrEnum):
    """Service type for invoice/offer line items."""

    SERVICE = "service"
    EXPENSE = "expense"


class Currency(_StrEnum):
    """Common currency codes."""

    EUR = "EUR"
    USD = "USD"
    CHF = "CHF"
    GBP = "GBP"


# ── Invoice ──────────────────────────────────────────────────────────────


class InvoiceStatus(_StrEnum):
    """Invoice status."""

    DRAFT = "draft"
    CREATED = "created"
    SENT = "sent"
    PARTIALLY_PAID = "partially_paid"
    PAID = "paid"
    OVERDUE = "overdue"
    IGNORED = "ignored"
    DISREGARDED = "disregarded"


class InvoiceChangeAddress(_StrEnum):
    """Address propagation target for invoices."""

    INVOICE = "invoice"
    PROJECT = "project"
    CUSTOMER = "customer"


# ── Offer ────────────────────────────────────────────────────────────────


class OfferStatus(_StrEnum):
    """Offer status."""

    CREATED = "created"
    SENT = "sent"
    ACCEPTED = "accepted"
    PARTIALLY_BILLED = "partially_billed"
    BILLED = "billed"
    ARCHIVED = "archived"


class OfferChangeAddress(_StrEnum):
    """Address propagation target for offers."""

    OFFER = "offer"
    CUSTOMER = "customer"


# ── Deal ─────────────────────────────────────────────────────────────────


class DealStatus(_StrEnum):
    """Deal/lead status."""

    POTENTIAL = "potential"
    PENDING = "pending"
    WON = "won"
    LOST = "lost"
    DROPPED = "dropped"


# ── Purchase ─────────────────────────────────────────────────────────────


class PurchaseStatus(_StrEnum):
    """Purchase status."""

    PENDING = "pending"
    ARCHIVED = "archived"


class ApprovalStatus(_StrEnum):
    """Approval status for purchases."""

    NONE = "none"
    APPROVED = "approved"
    DENIED = "denied"
    PENDING = "pending"


class PaymentMethod(_StrEnum):
    """Payment method for purchases."""

    BANK_TRANSFER = "bank_transfer"
    DIRECT_DEBIT = "direct_debit"
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    CASH = "cash"
    BANK_TRANSFER_SWISS_QR_ESR = "bank_transfer_swiss_qr_esr"


# ── Company ──────────────────────────────────────────────────────────────


class CompanyType(_StrEnum):
    """Company type."""

    CUSTOMER = "customer"
    SUPPLIER = "supplier"
    ORGANIZATION = "organization"


class InvoiceFormat(_StrEnum):
    """Company invoice format setting."""

    REGULAR_PDF = "regular_pdf"
    X_INVOICE = "x_invoice"
    ZUGFERD_X_INVOICE = "zugferd_x_invoice"


class DefaultPaymentMeans(_StrEnum):
    """Default payment means for companies."""

    NOT_DEFINED = "not_defined"
    CREDIT_TRANSFER = "credit_transfer"


# ── Project ──────────────────────────────────────────────────────────────


class BillingVariant(_StrEnum):
    """Project billing variant."""

    PROJECT = "project"
    TASK = "task"
    USER = "user"


# ── User ─────────────────────────────────────────────────────────────────


class UserLanguage(_StrEnum):
    """User interface language."""

    DE = "de"
    DE_AT = "de-AT"
    DE_CH = "de-CH"
    EN = "en"
    IT = "it"
    FR = "fr"


# ── Contact ──────────────────────────────────────────────────────────────


class Gender(_StrEnum):
    """Contact gender."""

    MALE = "M"
    FEMALE = "F"


# ── Activity ─────────────────────────────────────────────────────────────


class RemoteService(_StrEnum):
    """Remote service integration for activities."""

    TRELLO = "trello"
    JIRA = "jira"
    ASANA = "asana"
    BASECAMP = "basecamp"
    WUNDERLIST = "wunderlist"
    BASECAMP2 = "basecamp2"
    BASECAMP3 = "basecamp3"
    TOGGL = "toggl"
    MITE = "mite"
    GITHUB = "github"
    YOUTRACK = "youtrack"


# ── Comment ──────────────────────────────────────────────────────────────


class CommentableType(_StrEnum):
    """Types of objects that can have comments attached."""

    COMPANY = "Company"
    CONTACT = "Contact"
    DEAL = "Deal"
    DELIVERY_NOTE = "DeliveryNote"
    EXPENSE = "Expense"
    INVOICE = "Invoice"
    INVOICE_BOOKKEEPING_EXPORT = "InvoiceBookkeepingExport"
    INVOICE_DELETION = "InvoiceDeletion"
    INVOICE_REMINDER = "InvoiceReminder"
    OFFER = "Offer"
    OFFER_CONFIRMATION = "OfferConfirmation"
    PROJECT = "Project"
    PROJECT_GROUP = "ProjectGroup"
    PURCHASE = "Purchase"
    PURCHASE_BOOKKEEPING_EXPORT = "PurchaseBookkeepingExport"
    PURCHASE_DRAFT = "PurchaseDraft"
    RECEIPT = "Receipt"
    RECEIPT_REFUND_REQUEST = "ReceiptRefundRequest"
    RECURRING_EXPENSE = "RecurringExpense"
    UNIT = "Unit"
    USER = "User"
    USER_HOLIDAY_REQUEST = "UserHolidayRequest"


# ── Webhook ──────────────────────────────────────────────────────────────


class WebhookTarget(_StrEnum):
    """Resource types for webhook subscriptions."""

    ACTIVITY = "Activity"
    COMPANY = "Company"
    CONTACT = "Contact"
    PROJECT = "Project"
    INVOICE = "Invoice"
    OFFER = "Offer"
    DEAL = "Deal"
    EXPENSE = "Expense"


class WebhookEvent(_StrEnum):
    """Webhook event types."""

    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"


# ── Schedule / Absence ───────────────────────────────────────────────────


class AbsenceCode(IntEnum):
    """Absence type codes for schedules."""

    UNPLANNABLE = 1
    PUBLIC_HOLIDAY = 2
    SICK_DAY = 3
    HOLIDAY = 4
    ABSENCE = 5


class ScheduleSymbol(IntEnum):
    """Visual marker symbols for schedule entries."""

    HOME = 1
    BUILDING = 2
    CAR = 3
    GRADUATION_CAP = 4
    COCKTAIL = 5
    BELLS = 6
    BABY_CARRIAGE = 7
    USERS = 8
    MOON = 9
    INFO_CIRCLE = 10
    DOT_CIRCLE = 11
    EXCLAMATION_MARK = 12


class PlanningSymbol(IntEnum):
    """Visual marker symbols for planning entries (subset of ScheduleSymbol)."""

    HOME = 1
    BUILDING = 2
    CAR = 3
    GRADUATION_CAP = 4
    COCKTAIL = 5
    BELLS = 6
    BABY_CARRIAGE = 7
    USERS = 8
    MOON = 9
    INFO_CIRCLE = 10
