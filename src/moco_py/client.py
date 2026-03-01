"""Moco (sync) and AsyncMoco (async) client classes."""

from __future__ import annotations

import os
from functools import cached_property
from typing import TYPE_CHECKING, Any

import httpx

if TYPE_CHECKING:
    from .resources.account_custom_properties import (
        AccountCustomProperties,
        AsyncAccountCustomProperties,
    )
    from .resources.account_web_hooks import (
        AccountWebHooks,
        AsyncAccountWebHooks,
    )
    from .resources.activities import Activities, AsyncActivities
    from .resources.comments import AsyncComments, Comments
    from .resources.companies import AsyncCompanies, Companies
    from .resources.contacts import AsyncContacts, Contacts
    from .resources.deal_categories import (
        AsyncDealCategories,
        DealCategories,
    )
    from .resources.deals import AsyncDeals, Deals
    from .resources.employments import AsyncEmployments, Employments
    from .resources.holidays import AsyncHolidays, Holidays
    from .resources.invoice_bookkeeping_exports import (
        AsyncInvoiceBookkeepingExports,
        InvoiceBookkeepingExports,
    )
    from .resources.invoice_payments import (
        AsyncInvoicePayments,
        InvoicePayments,
    )
    from .resources.invoice_reminders import (
        AsyncInvoiceReminders,
        InvoiceReminders,
    )
    from .resources.invoices import AsyncInvoices, Invoices
    from .resources.offer_customer_approval import (
        AsyncOfferCustomerApprovals,
        OfferCustomerApprovals,
    )
    from .resources.offers import AsyncOffers, Offers
    from .resources.planning_entries import (
        AsyncPlanningEntries,
        PlanningEntries,
    )
    from .resources.presences import AsyncPresences, Presences
    from .resources.profile import AsyncProfileResource, ProfileResource
    from .resources.project_contracts import (
        AsyncProjectContracts,
        ProjectContracts,
    )
    from .resources.project_expenses import (
        AsyncProjectExpenses,
        ProjectExpenses,
    )
    from .resources.project_groups import AsyncProjectGroups, ProjectGroups
    from .resources.project_payment_schedules import (
        AsyncProjectPaymentSchedules,
        ProjectPaymentSchedules,
    )
    from .resources.project_recurring_expenses import (
        AsyncProjectRecurringExpenses,
        ProjectRecurringExpenses,
    )
    from .resources.project_tasks import AsyncProjectTasks, ProjectTasks
    from .resources.projects import AsyncProjects, Projects
    from .resources.purchase_bookkeeping_exports import (
        AsyncPurchaseBookkeepingExports,
        PurchaseBookkeepingExports,
    )
    from .resources.purchase_budgets import (
        AsyncPurchaseBudgets,
        PurchaseBudgets,
    )
    from .resources.purchase_categories import (
        AsyncPurchaseCategories,
        PurchaseCategories,
    )
    from .resources.purchase_drafts import (
        AsyncPurchaseDrafts,
        PurchaseDrafts,
    )
    from .resources.purchase_payments import (
        AsyncPurchasePayments,
        PurchasePayments,
    )
    from .resources.purchases import AsyncPurchases, Purchases
    from .resources.receipts import AsyncReceipts, Receipts
    from .resources.reports import AsyncReports, Reports
    from .resources.schedules import AsyncSchedules, Schedules
    from .resources.tags import AsyncTags, Tags
    from .resources.units import AsyncUnits, Units
    from .resources.user_roles import AsyncUserRoles, UserRoles
    from .resources.users import AsyncUsers, Users
    from .resources.vat_codes import (
        AsyncVatCodePurchases,
        AsyncVatCodeSales,
        VatCodePurchases,
        VatCodeSales,
    )
    from .resources.work_time_adjustments import (
        AsyncWorkTimeAdjustments,
        WorkTimeAdjustments,
    )

from ._constants import (
    BASE_URL_TEMPLATE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
    ENV_API_KEY,
    ENV_DOMAIN,
)
from ._transport import AsyncTransport, SyncTransport
from .exceptions import MocoError


class Moco:
    """Synchronous client for the MOCO API.

    Args:
        api_key: API key. Falls back to MOCO_API_KEY env var.
        domain: MOCO subdomain (e.g. "yourcompany"). Falls back to MOCO_DOMAIN env var.
        base_url: Override the full base URL (skips domain requirement).
        timeout: Request timeout in seconds.
        max_retries: Maximum number of retries for transient errors.
        default_headers: Additional headers to send with every request.
        impersonate_user_id: User ID for impersonation via X-IMPERSONATE-USER-ID.
        http_client: Custom httpx.Client instance.
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        domain: str | None = None,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: dict[str, str] | None = None,
        impersonate_user_id: int | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        resolved_api_key = api_key or os.environ.get(ENV_API_KEY)
        if not resolved_api_key:
            raise MocoError(f"api_key must be provided or set {ENV_API_KEY}")

        resolved_domain = domain or os.environ.get(ENV_DOMAIN)
        if not base_url and not resolved_domain:
            raise MocoError(
                f"domain must be provided or set the {ENV_DOMAIN} environment variable"
            )

        resolved_base_url = base_url or BASE_URL_TEMPLATE.format(domain=resolved_domain)

        headers: dict[str, str] = dict(default_headers or {})
        if impersonate_user_id is not None:
            headers["X-IMPERSONATE-USER-ID"] = str(impersonate_user_id)

        self._transport = SyncTransport(
            base_url=resolved_base_url,
            api_key=resolved_api_key,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=headers or None,
            http_client=http_client,
        )

    # -- Resource properties --

    @cached_property
    def activities(self) -> Activities:
        from .resources.activities import Activities

        return Activities(self._transport)

    @cached_property
    def comments(self) -> Comments:
        from .resources.comments import Comments

        return Comments(self._transport)

    @cached_property
    def companies(self) -> Companies:
        from .resources.companies import Companies

        return Companies(self._transport)

    @cached_property
    def contacts(self) -> Contacts:
        from .resources.contacts import Contacts

        return Contacts(self._transport)

    @cached_property
    def deal_categories(self) -> DealCategories:
        from .resources.deal_categories import DealCategories

        return DealCategories(self._transport)

    @cached_property
    def deals(self) -> Deals:
        from .resources.deals import Deals

        return Deals(self._transport)

    @cached_property
    def employments(self) -> Employments:
        from .resources.employments import Employments

        return Employments(self._transport)

    @cached_property
    def holidays(self) -> Holidays:
        from .resources.holidays import Holidays

        return Holidays(self._transport)

    @cached_property
    def invoices(self) -> Invoices:
        from .resources.invoices import Invoices

        return Invoices(self._transport)

    @cached_property
    def invoice_bookkeeping_exports(self) -> InvoiceBookkeepingExports:
        from .resources.invoice_bookkeeping_exports import InvoiceBookkeepingExports

        return InvoiceBookkeepingExports(self._transport)

    @cached_property
    def invoice_payments(self) -> InvoicePayments:
        from .resources.invoice_payments import InvoicePayments

        return InvoicePayments(self._transport)

    @cached_property
    def invoice_reminders(self) -> InvoiceReminders:
        from .resources.invoice_reminders import InvoiceReminders

        return InvoiceReminders(self._transport)

    @cached_property
    def offers(self) -> Offers:
        from .resources.offers import Offers

        return Offers(self._transport)

    @cached_property
    def offer_customer_approvals(self) -> OfferCustomerApprovals:
        from .resources.offer_customer_approval import OfferCustomerApprovals

        return OfferCustomerApprovals(self._transport)

    @cached_property
    def planning_entries(self) -> PlanningEntries:
        from .resources.planning_entries import PlanningEntries

        return PlanningEntries(self._transport)

    @cached_property
    def presences(self) -> Presences:
        from .resources.presences import Presences

        return Presences(self._transport)

    @cached_property
    def profile(self) -> ProfileResource:
        from .resources.profile import ProfileResource

        return ProfileResource(self._transport)

    @cached_property
    def projects(self) -> Projects:
        from .resources.projects import Projects

        return Projects(self._transport)

    @cached_property
    def project_contracts(self) -> ProjectContracts:
        from .resources.project_contracts import ProjectContracts

        return ProjectContracts(self._transport)

    @cached_property
    def project_expenses(self) -> ProjectExpenses:
        from .resources.project_expenses import ProjectExpenses

        return ProjectExpenses(self._transport)

    @cached_property
    def project_groups(self) -> ProjectGroups:
        from .resources.project_groups import ProjectGroups

        return ProjectGroups(self._transport)

    @cached_property
    def project_payment_schedules(self) -> ProjectPaymentSchedules:
        from .resources.project_payment_schedules import ProjectPaymentSchedules

        return ProjectPaymentSchedules(self._transport)

    @cached_property
    def project_recurring_expenses(self) -> ProjectRecurringExpenses:
        from .resources.project_recurring_expenses import ProjectRecurringExpenses

        return ProjectRecurringExpenses(self._transport)

    @cached_property
    def project_tasks(self) -> ProjectTasks:
        from .resources.project_tasks import ProjectTasks

        return ProjectTasks(self._transport)

    @cached_property
    def purchases(self) -> Purchases:
        from .resources.purchases import Purchases

        return Purchases(self._transport)

    @cached_property
    def purchase_bookkeeping_exports(self) -> PurchaseBookkeepingExports:
        from .resources.purchase_bookkeeping_exports import PurchaseBookkeepingExports

        return PurchaseBookkeepingExports(self._transport)

    @cached_property
    def purchase_budgets(self) -> PurchaseBudgets:
        from .resources.purchase_budgets import PurchaseBudgets

        return PurchaseBudgets(self._transport)

    @cached_property
    def purchase_categories(self) -> PurchaseCategories:
        from .resources.purchase_categories import PurchaseCategories

        return PurchaseCategories(self._transport)

    @cached_property
    def purchase_drafts(self) -> PurchaseDrafts:
        from .resources.purchase_drafts import PurchaseDrafts

        return PurchaseDrafts(self._transport)

    @cached_property
    def purchase_payments(self) -> PurchasePayments:
        from .resources.purchase_payments import PurchasePayments

        return PurchasePayments(self._transport)

    @cached_property
    def receipts(self) -> Receipts:
        from .resources.receipts import Receipts

        return Receipts(self._transport)

    @cached_property
    def reports(self) -> Reports:
        from .resources.reports import Reports

        return Reports(self._transport)

    @cached_property
    def schedules(self) -> Schedules:
        from .resources.schedules import Schedules

        return Schedules(self._transport)

    @cached_property
    def tags(self) -> Tags:
        from .resources.tags import Tags

        return Tags(self._transport)

    @cached_property
    def units(self) -> Units:
        from .resources.units import Units

        return Units(self._transport)

    @cached_property
    def user_roles(self) -> UserRoles:
        from .resources.user_roles import UserRoles

        return UserRoles(self._transport)

    @cached_property
    def users(self) -> Users:
        from .resources.users import Users

        return Users(self._transport)

    @cached_property
    def vat_code_sales(self) -> VatCodeSales:
        from .resources.vat_codes import VatCodeSales

        return VatCodeSales(self._transport)

    @cached_property
    def vat_code_purchases(self) -> VatCodePurchases:
        from .resources.vat_codes import VatCodePurchases

        return VatCodePurchases(self._transport)

    @cached_property
    def work_time_adjustments(self) -> WorkTimeAdjustments:
        from .resources.work_time_adjustments import WorkTimeAdjustments

        return WorkTimeAdjustments(self._transport)

    @cached_property
    def account_custom_properties(self) -> AccountCustomProperties:
        from .resources.account_custom_properties import AccountCustomProperties

        return AccountCustomProperties(self._transport)

    @cached_property
    def account_web_hooks(self) -> AccountWebHooks:
        from .resources.account_web_hooks import AccountWebHooks

        return AccountWebHooks(self._transport)

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._transport.close()

    def __enter__(self) -> Moco:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()


class AsyncMoco:
    """Asynchronous client for the MOCO API.

    Args:
        api_key: API key. Falls back to MOCO_API_KEY env var.
        domain: MOCO subdomain (e.g. "yourcompany"). Falls back to MOCO_DOMAIN env var.
        base_url: Override the full base URL (skips domain requirement).
        timeout: Request timeout in seconds.
        max_retries: Maximum number of retries for transient errors.
        default_headers: Additional headers to send with every request.
        impersonate_user_id: User ID for impersonation via X-IMPERSONATE-USER-ID.
        http_client: Custom httpx.AsyncClient instance.
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        domain: str | None = None,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: dict[str, str] | None = None,
        impersonate_user_id: int | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        resolved_api_key = api_key or os.environ.get(ENV_API_KEY)
        if not resolved_api_key:
            raise MocoError(f"api_key must be provided or set {ENV_API_KEY}")

        resolved_domain = domain or os.environ.get(ENV_DOMAIN)
        if not base_url and not resolved_domain:
            raise MocoError(
                f"domain must be provided or set the {ENV_DOMAIN} environment variable"
            )

        resolved_base_url = base_url or BASE_URL_TEMPLATE.format(domain=resolved_domain)

        headers: dict[str, str] = dict(default_headers or {})
        if impersonate_user_id is not None:
            headers["X-IMPERSONATE-USER-ID"] = str(impersonate_user_id)

        self._transport = AsyncTransport(
            base_url=resolved_base_url,
            api_key=resolved_api_key,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=headers or None,
            http_client=http_client,
        )

    # -- Resource properties --

    @cached_property
    def activities(self) -> AsyncActivities:
        from .resources.activities import AsyncActivities

        return AsyncActivities(self._transport)

    @cached_property
    def comments(self) -> AsyncComments:
        from .resources.comments import AsyncComments

        return AsyncComments(self._transport)

    @cached_property
    def companies(self) -> AsyncCompanies:
        from .resources.companies import AsyncCompanies

        return AsyncCompanies(self._transport)

    @cached_property
    def contacts(self) -> AsyncContacts:
        from .resources.contacts import AsyncContacts

        return AsyncContacts(self._transport)

    @cached_property
    def deal_categories(self) -> AsyncDealCategories:
        from .resources.deal_categories import AsyncDealCategories

        return AsyncDealCategories(self._transport)

    @cached_property
    def deals(self) -> AsyncDeals:
        from .resources.deals import AsyncDeals

        return AsyncDeals(self._transport)

    @cached_property
    def employments(self) -> AsyncEmployments:
        from .resources.employments import AsyncEmployments

        return AsyncEmployments(self._transport)

    @cached_property
    def holidays(self) -> AsyncHolidays:
        from .resources.holidays import AsyncHolidays

        return AsyncHolidays(self._transport)

    @cached_property
    def invoices(self) -> AsyncInvoices:
        from .resources.invoices import AsyncInvoices

        return AsyncInvoices(self._transport)

    @cached_property
    def invoice_bookkeeping_exports(self) -> AsyncInvoiceBookkeepingExports:
        from .resources.invoice_bookkeeping_exports import (
            AsyncInvoiceBookkeepingExports,
        )

        return AsyncInvoiceBookkeepingExports(self._transport)

    @cached_property
    def invoice_payments(self) -> AsyncInvoicePayments:
        from .resources.invoice_payments import AsyncInvoicePayments

        return AsyncInvoicePayments(self._transport)

    @cached_property
    def invoice_reminders(self) -> AsyncInvoiceReminders:
        from .resources.invoice_reminders import AsyncInvoiceReminders

        return AsyncInvoiceReminders(self._transport)

    @cached_property
    def offers(self) -> AsyncOffers:
        from .resources.offers import AsyncOffers

        return AsyncOffers(self._transport)

    @cached_property
    def offer_customer_approvals(self) -> AsyncOfferCustomerApprovals:
        from .resources.offer_customer_approval import AsyncOfferCustomerApprovals

        return AsyncOfferCustomerApprovals(self._transport)

    @cached_property
    def planning_entries(self) -> AsyncPlanningEntries:
        from .resources.planning_entries import AsyncPlanningEntries

        return AsyncPlanningEntries(self._transport)

    @cached_property
    def presences(self) -> AsyncPresences:
        from .resources.presences import AsyncPresences

        return AsyncPresences(self._transport)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        from .resources.profile import AsyncProfileResource

        return AsyncProfileResource(self._transport)

    @cached_property
    def projects(self) -> AsyncProjects:
        from .resources.projects import AsyncProjects

        return AsyncProjects(self._transport)

    @cached_property
    def project_contracts(self) -> AsyncProjectContracts:
        from .resources.project_contracts import AsyncProjectContracts

        return AsyncProjectContracts(self._transport)

    @cached_property
    def project_expenses(self) -> AsyncProjectExpenses:
        from .resources.project_expenses import AsyncProjectExpenses

        return AsyncProjectExpenses(self._transport)

    @cached_property
    def project_groups(self) -> AsyncProjectGroups:
        from .resources.project_groups import AsyncProjectGroups

        return AsyncProjectGroups(self._transport)

    @cached_property
    def project_payment_schedules(self) -> AsyncProjectPaymentSchedules:
        from .resources.project_payment_schedules import AsyncProjectPaymentSchedules

        return AsyncProjectPaymentSchedules(self._transport)

    @cached_property
    def project_recurring_expenses(self) -> AsyncProjectRecurringExpenses:
        from .resources.project_recurring_expenses import AsyncProjectRecurringExpenses

        return AsyncProjectRecurringExpenses(self._transport)

    @cached_property
    def project_tasks(self) -> AsyncProjectTasks:
        from .resources.project_tasks import AsyncProjectTasks

        return AsyncProjectTasks(self._transport)

    @cached_property
    def purchases(self) -> AsyncPurchases:
        from .resources.purchases import AsyncPurchases

        return AsyncPurchases(self._transport)

    @cached_property
    def purchase_bookkeeping_exports(self) -> AsyncPurchaseBookkeepingExports:
        from .resources.purchase_bookkeeping_exports import (
            AsyncPurchaseBookkeepingExports,
        )

        return AsyncPurchaseBookkeepingExports(self._transport)

    @cached_property
    def purchase_budgets(self) -> AsyncPurchaseBudgets:
        from .resources.purchase_budgets import AsyncPurchaseBudgets

        return AsyncPurchaseBudgets(self._transport)

    @cached_property
    def purchase_categories(self) -> AsyncPurchaseCategories:
        from .resources.purchase_categories import AsyncPurchaseCategories

        return AsyncPurchaseCategories(self._transport)

    @cached_property
    def purchase_drafts(self) -> AsyncPurchaseDrafts:
        from .resources.purchase_drafts import AsyncPurchaseDrafts

        return AsyncPurchaseDrafts(self._transport)

    @cached_property
    def purchase_payments(self) -> AsyncPurchasePayments:
        from .resources.purchase_payments import AsyncPurchasePayments

        return AsyncPurchasePayments(self._transport)

    @cached_property
    def receipts(self) -> AsyncReceipts:
        from .resources.receipts import AsyncReceipts

        return AsyncReceipts(self._transport)

    @cached_property
    def reports(self) -> AsyncReports:
        from .resources.reports import AsyncReports

        return AsyncReports(self._transport)

    @cached_property
    def schedules(self) -> AsyncSchedules:
        from .resources.schedules import AsyncSchedules

        return AsyncSchedules(self._transport)

    @cached_property
    def tags(self) -> AsyncTags:
        from .resources.tags import AsyncTags

        return AsyncTags(self._transport)

    @cached_property
    def units(self) -> AsyncUnits:
        from .resources.units import AsyncUnits

        return AsyncUnits(self._transport)

    @cached_property
    def user_roles(self) -> AsyncUserRoles:
        from .resources.user_roles import AsyncUserRoles

        return AsyncUserRoles(self._transport)

    @cached_property
    def users(self) -> AsyncUsers:
        from .resources.users import AsyncUsers

        return AsyncUsers(self._transport)

    @cached_property
    def vat_code_sales(self) -> AsyncVatCodeSales:
        from .resources.vat_codes import AsyncVatCodeSales

        return AsyncVatCodeSales(self._transport)

    @cached_property
    def vat_code_purchases(self) -> AsyncVatCodePurchases:
        from .resources.vat_codes import AsyncVatCodePurchases

        return AsyncVatCodePurchases(self._transport)

    @cached_property
    def work_time_adjustments(self) -> AsyncWorkTimeAdjustments:
        from .resources.work_time_adjustments import AsyncWorkTimeAdjustments

        return AsyncWorkTimeAdjustments(self._transport)

    @cached_property
    def account_custom_properties(self) -> AsyncAccountCustomProperties:
        from .resources.account_custom_properties import AsyncAccountCustomProperties

        return AsyncAccountCustomProperties(self._transport)

    @cached_property
    def account_web_hooks(self) -> AsyncAccountWebHooks:
        from .resources.account_web_hooks import AsyncAccountWebHooks

        return AsyncAccountWebHooks(self._transport)

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        await self._transport.close()

    async def __aenter__(self) -> AsyncMoco:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
