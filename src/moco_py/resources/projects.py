"""Projects resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import BillingVariant
from ..types.projects import (
    AssignedProject,
    Project,
    ProjectReport,
    ProjectShareResponse,
)


class Projects(SyncResource):
    """Synchronous projects resource."""

    def list(
        self,
        *,
        include_archived: bool | None = None,
        include_company: bool | None = None,
        leader_id: int | str | None = None,
        company_id: int | str | None = None,
        created_from: str | None = None,
        created_to: str | None = None,
        updated_from: str | None = None,
        updated_to: str | None = None,
        tags: str | None = None,
        identifier: str | None = None,
        retainer: bool | None = None,
        project_group_id: int | str | None = None,
        deal_id: int | str | None = None,
        sort_by: str | None = None,
    ) -> SyncPage[Project]:
        """Retrieve all projects."""
        params: dict[str, Any] = {}
        if include_archived is not None:
            params["include_archived"] = include_archived
        if include_company is not None:
            params["include_company"] = include_company
        if leader_id is not None:
            params["leader_id"] = leader_id
        if company_id is not None:
            params["company_id"] = company_id
        if created_from is not None:
            params["created_from"] = created_from
        if created_to is not None:
            params["created_to"] = created_to
        if updated_from is not None:
            params["updated_from"] = updated_from
        if updated_to is not None:
            params["updated_to"] = updated_to
        if tags is not None:
            params["tags"] = tags
        if identifier is not None:
            params["identifier"] = identifier
        if retainer is not None:
            params["retainer"] = retainer
        if project_group_id is not None:
            params["project_group_id"] = project_group_id
        if deal_id is not None:
            params["deal_id"] = deal_id
        if sort_by is not None:
            params["sort_by"] = sort_by
        return self._get_list("/projects", params=params or None, cast_to=Project)

    def assigned(self, *, active: bool | None = None) -> SyncPage[AssignedProject]:
        """Retrieve all projects assigned to the user."""
        params: dict[str, Any] = {}
        if active is not None:
            params["active"] = active
        return self._get_list(
            "/projects/assigned", params=params or None, cast_to=AssignedProject
        )

    def get(self, project_id: int) -> MocoResponse[Project]:
        """Retrieve a single project."""
        return self._get(f"/projects/{project_id}", cast_to=Project)

    def create(
        self,
        *,
        name: str,
        currency: str,
        start_date: str,
        finish_date: str,
        fixed_price: bool,
        retainer: bool,
        leader_id: int,
        customer_id: int,
        identifier: str | None = None,
        co_leader_id: int | None = None,
        deal_id: int | None = None,
        project_group_id: int | None = None,
        contact_id: int | None = None,
        secondary_contact_id: int | None = None,
        billing_contact_id: int | None = None,
        billing_address: str | None = None,
        billing_email_to: str | None = None,
        billing_email_cc: str | None = None,
        billing_notes: str | None = None,
        setting_include_time_report: bool | None = None,
        billing_variant: BillingVariant | None = None,
        hourly_rate: float | None = None,
        budget: float | None = None,
        budget_monthly: float | None = None,
        budget_expenses: float | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        custom_properties: dict[str, Any] | None = None,
        info: str | None = None,
        skip_favorite: bool | None = None,
        retainer_billing_date: int | None = None,
        retainer_billing_title: str | None = None,
        retainer_billing_description: str | None = None,
    ) -> MocoResponse[Project]:
        """Create a project."""
        data: dict[str, Any] = {
            "name": name,
            "currency": currency,
            "start_date": start_date,
            "finish_date": finish_date,
            "fixed_price": fixed_price,
            "retainer": retainer,
            "leader_id": leader_id,
            "customer_id": customer_id,
        }
        if identifier is not None:
            data["identifier"] = identifier
        if co_leader_id is not None:
            data["co_leader_id"] = co_leader_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        if project_group_id is not None:
            data["project_group_id"] = project_group_id
        if contact_id is not None:
            data["contact_id"] = contact_id
        if secondary_contact_id is not None:
            data["secondary_contact_id"] = secondary_contact_id
        if billing_contact_id is not None:
            data["billing_contact_id"] = billing_contact_id
        if billing_address is not None:
            data["billing_address"] = billing_address
        if billing_email_to is not None:
            data["billing_email_to"] = billing_email_to
        if billing_email_cc is not None:
            data["billing_email_cc"] = billing_email_cc
        if billing_notes is not None:
            data["billing_notes"] = billing_notes
        if setting_include_time_report is not None:
            data["setting_include_time_report"] = setting_include_time_report
        if billing_variant is not None:
            data["billing_variant"] = billing_variant
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        if budget is not None:
            data["budget"] = budget
        if budget_monthly is not None:
            data["budget_monthly"] = budget_monthly
        if budget_expenses is not None:
            data["budget_expenses"] = budget_expenses
        if tags is not None:
            data["tags"] = tags
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if info is not None:
            data["info"] = info
        if skip_favorite is not None:
            data["skip_favorite"] = skip_favorite
        if retainer_billing_date is not None:
            data["retainer_billing_date"] = retainer_billing_date
        if retainer_billing_title is not None:
            data["retainer_billing_title"] = retainer_billing_title
        if retainer_billing_description is not None:
            data["retainer_billing_description"] = retainer_billing_description
        return self._post("/projects", json_data=data, cast_to=Project)

    def update(
        self,
        project_id: int,
        *,
        name: str | None = None,
        start_date: str | None = None,
        finish_date: str | None = None,
        fixed_price: bool | None = None,
        retainer: bool | None = None,
        leader_id: int | None = None,
        customer_id: int | None = None,
        identifier: str | None = None,
        co_leader_id: int | None = None,
        deal_id: int | None = None,
        project_group_id: int | None = None,
        contact_id: int | None = None,
        secondary_contact_id: int | None = None,
        billing_contact_id: int | None = None,
        billing_address: str | None = None,
        billing_email_to: str | None = None,
        billing_email_cc: str | None = None,
        billing_notes: str | None = None,
        setting_include_time_report: bool | None = None,
        billing_variant: BillingVariant | None = None,
        hourly_rate: float | None = None,
        budget: float | None = None,
        budget_monthly: float | None = None,
        budget_expenses: float | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        custom_properties: dict[str, Any] | None = None,
        info: str | None = None,
    ) -> MocoResponse[Project]:
        """Update a project."""
        data: dict[str, Any] = {}
        if name is not None:
            data["name"] = name
        if start_date is not None:
            data["start_date"] = start_date
        if finish_date is not None:
            data["finish_date"] = finish_date
        if fixed_price is not None:
            data["fixed_price"] = fixed_price
        if retainer is not None:
            data["retainer"] = retainer
        if leader_id is not None:
            data["leader_id"] = leader_id
        if customer_id is not None:
            data["customer_id"] = customer_id
        if identifier is not None:
            data["identifier"] = identifier
        if co_leader_id is not None:
            data["co_leader_id"] = co_leader_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        if project_group_id is not None:
            data["project_group_id"] = project_group_id
        if contact_id is not None:
            data["contact_id"] = contact_id
        if secondary_contact_id is not None:
            data["secondary_contact_id"] = secondary_contact_id
        if billing_contact_id is not None:
            data["billing_contact_id"] = billing_contact_id
        if billing_address is not None:
            data["billing_address"] = billing_address
        if billing_email_to is not None:
            data["billing_email_to"] = billing_email_to
        if billing_email_cc is not None:
            data["billing_email_cc"] = billing_email_cc
        if billing_notes is not None:
            data["billing_notes"] = billing_notes
        if setting_include_time_report is not None:
            data["setting_include_time_report"] = setting_include_time_report
        if billing_variant is not None:
            data["billing_variant"] = billing_variant
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        if budget is not None:
            data["budget"] = budget
        if budget_monthly is not None:
            data["budget_monthly"] = budget_monthly
        if budget_expenses is not None:
            data["budget_expenses"] = budget_expenses
        if tags is not None:
            data["tags"] = tags
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if info is not None:
            data["info"] = info
        return self._put(f"/projects/{project_id}", json_data=data, cast_to=Project)

    def delete(self, project_id: int) -> MocoResponse[None]:
        """Delete a project."""
        return self._delete(f"/projects/{project_id}")

    def archive(self, project_id: int) -> MocoResponse[Project]:
        """Archive a project."""
        return self._put(f"/projects/{project_id}/archive", cast_to=Project)

    def unarchive(self, project_id: int) -> MocoResponse[Project]:
        """Unarchive a project."""
        return self._put(f"/projects/{project_id}/unarchive", cast_to=Project)

    def report(self, project_id: int) -> MocoResponse[ProjectReport]:
        """Retrieve a project report."""
        return self._get(f"/projects/{project_id}/report", cast_to=ProjectReport)

    def share(self, project_id: int) -> MocoResponse[ProjectShareResponse]:
        """Activate project report sharing."""
        return self._put(f"/projects/{project_id}/share", cast_to=ProjectShareResponse)

    def disable_share(self, project_id: int) -> MocoResponse[ProjectShareResponse]:
        """Deactivate project report sharing."""
        return self._put(
            f"/projects/{project_id}/disable_share", cast_to=ProjectShareResponse
        )

    def assign_project_group(
        self, project_id: int, *, project_group_id: int
    ) -> MocoResponse[Project]:
        """Assign a project to a project group."""
        return self._put(
            f"/projects/{project_id}/assign_project_group",
            json_data={"project_group_id": project_group_id},
            cast_to=Project,
        )

    def unassign_project_group(self, project_id: int) -> MocoResponse[Project]:
        """Unassign a project from its project group."""
        return self._put(
            f"/projects/{project_id}/unassign_project_group", cast_to=Project
        )


class AsyncProjects(AsyncResource):
    """Asynchronous projects resource."""

    async def list(
        self,
        *,
        include_archived: bool | None = None,
        include_company: bool | None = None,
        leader_id: int | str | None = None,
        company_id: int | str | None = None,
        created_from: str | None = None,
        created_to: str | None = None,
        updated_from: str | None = None,
        updated_to: str | None = None,
        tags: str | None = None,
        identifier: str | None = None,
        retainer: bool | None = None,
        project_group_id: int | str | None = None,
        deal_id: int | str | None = None,
        sort_by: str | None = None,
    ) -> AsyncPage[Project]:
        """Retrieve all projects."""
        params: dict[str, Any] = {}
        if include_archived is not None:
            params["include_archived"] = include_archived
        if include_company is not None:
            params["include_company"] = include_company
        if leader_id is not None:
            params["leader_id"] = leader_id
        if company_id is not None:
            params["company_id"] = company_id
        if created_from is not None:
            params["created_from"] = created_from
        if created_to is not None:
            params["created_to"] = created_to
        if updated_from is not None:
            params["updated_from"] = updated_from
        if updated_to is not None:
            params["updated_to"] = updated_to
        if tags is not None:
            params["tags"] = tags
        if identifier is not None:
            params["identifier"] = identifier
        if retainer is not None:
            params["retainer"] = retainer
        if project_group_id is not None:
            params["project_group_id"] = project_group_id
        if deal_id is not None:
            params["deal_id"] = deal_id
        if sort_by is not None:
            params["sort_by"] = sort_by
        return await self._get_list("/projects", params=params or None, cast_to=Project)

    async def assigned(
        self, *, active: bool | None = None
    ) -> AsyncPage[AssignedProject]:
        """Retrieve all projects assigned to the user."""
        params: dict[str, Any] = {}
        if active is not None:
            params["active"] = active
        return await self._get_list(
            "/projects/assigned", params=params or None, cast_to=AssignedProject
        )

    async def get(self, project_id: int) -> MocoResponse[Project]:
        """Retrieve a single project."""
        return await self._get(f"/projects/{project_id}", cast_to=Project)

    async def create(
        self,
        *,
        name: str,
        currency: str,
        start_date: str,
        finish_date: str,
        fixed_price: bool,
        retainer: bool,
        leader_id: int,
        customer_id: int,
        identifier: str | None = None,
        co_leader_id: int | None = None,
        deal_id: int | None = None,
        project_group_id: int | None = None,
        contact_id: int | None = None,
        secondary_contact_id: int | None = None,
        billing_contact_id: int | None = None,
        billing_address: str | None = None,
        billing_email_to: str | None = None,
        billing_email_cc: str | None = None,
        billing_notes: str | None = None,
        setting_include_time_report: bool | None = None,
        billing_variant: BillingVariant | None = None,
        hourly_rate: float | None = None,
        budget: float | None = None,
        budget_monthly: float | None = None,
        budget_expenses: float | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        custom_properties: dict[str, Any] | None = None,
        info: str | None = None,
        skip_favorite: bool | None = None,
        retainer_billing_date: int | None = None,
        retainer_billing_title: str | None = None,
        retainer_billing_description: str | None = None,
    ) -> MocoResponse[Project]:
        """Create a project."""
        data: dict[str, Any] = {
            "name": name,
            "currency": currency,
            "start_date": start_date,
            "finish_date": finish_date,
            "fixed_price": fixed_price,
            "retainer": retainer,
            "leader_id": leader_id,
            "customer_id": customer_id,
        }
        if identifier is not None:
            data["identifier"] = identifier
        if co_leader_id is not None:
            data["co_leader_id"] = co_leader_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        if project_group_id is not None:
            data["project_group_id"] = project_group_id
        if contact_id is not None:
            data["contact_id"] = contact_id
        if secondary_contact_id is not None:
            data["secondary_contact_id"] = secondary_contact_id
        if billing_contact_id is not None:
            data["billing_contact_id"] = billing_contact_id
        if billing_address is not None:
            data["billing_address"] = billing_address
        if billing_email_to is not None:
            data["billing_email_to"] = billing_email_to
        if billing_email_cc is not None:
            data["billing_email_cc"] = billing_email_cc
        if billing_notes is not None:
            data["billing_notes"] = billing_notes
        if setting_include_time_report is not None:
            data["setting_include_time_report"] = setting_include_time_report
        if billing_variant is not None:
            data["billing_variant"] = billing_variant
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        if budget is not None:
            data["budget"] = budget
        if budget_monthly is not None:
            data["budget_monthly"] = budget_monthly
        if budget_expenses is not None:
            data["budget_expenses"] = budget_expenses
        if tags is not None:
            data["tags"] = tags
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if info is not None:
            data["info"] = info
        if skip_favorite is not None:
            data["skip_favorite"] = skip_favorite
        if retainer_billing_date is not None:
            data["retainer_billing_date"] = retainer_billing_date
        if retainer_billing_title is not None:
            data["retainer_billing_title"] = retainer_billing_title
        if retainer_billing_description is not None:
            data["retainer_billing_description"] = retainer_billing_description
        return await self._post("/projects", json_data=data, cast_to=Project)

    async def update(
        self,
        project_id: int,
        *,
        name: str | None = None,
        start_date: str | None = None,
        finish_date: str | None = None,
        fixed_price: bool | None = None,
        retainer: bool | None = None,
        leader_id: int | None = None,
        customer_id: int | None = None,
        identifier: str | None = None,
        co_leader_id: int | None = None,
        deal_id: int | None = None,
        project_group_id: int | None = None,
        contact_id: int | None = None,
        secondary_contact_id: int | None = None,
        billing_contact_id: int | None = None,
        billing_address: str | None = None,
        billing_email_to: str | None = None,
        billing_email_cc: str | None = None,
        billing_notes: str | None = None,
        setting_include_time_report: bool | None = None,
        billing_variant: BillingVariant | None = None,
        hourly_rate: float | None = None,
        budget: float | None = None,
        budget_monthly: float | None = None,
        budget_expenses: float | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        custom_properties: dict[str, Any] | None = None,
        info: str | None = None,
    ) -> MocoResponse[Project]:
        """Update a project."""
        data: dict[str, Any] = {}
        if name is not None:
            data["name"] = name
        if start_date is not None:
            data["start_date"] = start_date
        if finish_date is not None:
            data["finish_date"] = finish_date
        if fixed_price is not None:
            data["fixed_price"] = fixed_price
        if retainer is not None:
            data["retainer"] = retainer
        if leader_id is not None:
            data["leader_id"] = leader_id
        if customer_id is not None:
            data["customer_id"] = customer_id
        if identifier is not None:
            data["identifier"] = identifier
        if co_leader_id is not None:
            data["co_leader_id"] = co_leader_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        if project_group_id is not None:
            data["project_group_id"] = project_group_id
        if contact_id is not None:
            data["contact_id"] = contact_id
        if secondary_contact_id is not None:
            data["secondary_contact_id"] = secondary_contact_id
        if billing_contact_id is not None:
            data["billing_contact_id"] = billing_contact_id
        if billing_address is not None:
            data["billing_address"] = billing_address
        if billing_email_to is not None:
            data["billing_email_to"] = billing_email_to
        if billing_email_cc is not None:
            data["billing_email_cc"] = billing_email_cc
        if billing_notes is not None:
            data["billing_notes"] = billing_notes
        if setting_include_time_report is not None:
            data["setting_include_time_report"] = setting_include_time_report
        if billing_variant is not None:
            data["billing_variant"] = billing_variant
        if hourly_rate is not None:
            data["hourly_rate"] = hourly_rate
        if budget is not None:
            data["budget"] = budget
        if budget_monthly is not None:
            data["budget_monthly"] = budget_monthly
        if budget_expenses is not None:
            data["budget_expenses"] = budget_expenses
        if tags is not None:
            data["tags"] = tags
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if info is not None:
            data["info"] = info
        return await self._put(
            f"/projects/{project_id}", json_data=data, cast_to=Project
        )

    async def delete(self, project_id: int) -> MocoResponse[None]:
        """Delete a project."""
        return await self._delete(f"/projects/{project_id}")

    async def archive(self, project_id: int) -> MocoResponse[Project]:
        """Archive a project."""
        return await self._put(f"/projects/{project_id}/archive", cast_to=Project)

    async def unarchive(self, project_id: int) -> MocoResponse[Project]:
        """Unarchive a project."""
        return await self._put(f"/projects/{project_id}/unarchive", cast_to=Project)

    async def report(self, project_id: int) -> MocoResponse[ProjectReport]:
        """Retrieve a project report."""
        return await self._get(f"/projects/{project_id}/report", cast_to=ProjectReport)

    async def share(self, project_id: int) -> MocoResponse[ProjectShareResponse]:
        """Activate project report sharing."""
        return await self._put(
            f"/projects/{project_id}/share", cast_to=ProjectShareResponse
        )

    async def disable_share(
        self, project_id: int
    ) -> MocoResponse[ProjectShareResponse]:
        """Deactivate project report sharing."""
        return await self._put(
            f"/projects/{project_id}/disable_share", cast_to=ProjectShareResponse
        )

    async def assign_project_group(
        self, project_id: int, *, project_group_id: int
    ) -> MocoResponse[Project]:
        """Assign a project to a project group."""
        return await self._put(
            f"/projects/{project_id}/assign_project_group",
            json_data={"project_group_id": project_group_id},
            cast_to=Project,
        )

    async def unassign_project_group(self, project_id: int) -> MocoResponse[Project]:
        """Unassign a project from its project group."""
        return await self._put(
            f"/projects/{project_id}/unassign_project_group", cast_to=Project
        )
