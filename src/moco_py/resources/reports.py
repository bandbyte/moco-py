"""Reports resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from ..types.reports import (
    AbsenceEntry,
    CashflowEntry,
    FinanceEntry,
    PlannedVsTrackedEntry,
    UtilizationEntry,
)


class Reports(SyncResource):
    """Synchronous reports resource."""

    def absences(
        self,
        *,
        active: bool | None = None,
        year: int | None = None,
    ) -> SyncPage[AbsenceEntry]:
        """Retrieve the absences report."""
        params: dict[str, Any] = {}
        if active is not None:
            params["active"] = active
        if year is not None:
            params["year"] = year
        return self._get_list("/report/absences", params=params, cast_to=AbsenceEntry)

    def cashflow(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        term: str | None = None,
    ) -> SyncPage[CashflowEntry]:
        """Retrieve the cashflow report."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if term is not None:
            params["term"] = term
        return self._get_list("/report/cashflow", params=params, cast_to=CashflowEntry)

    def finance(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        term: str | None = None,
    ) -> SyncPage[FinanceEntry]:
        """Retrieve the finance report."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if term is not None:
            params["term"] = term
        return self._get_list("/report/finance", params=params, cast_to=FinanceEntry)

    def planned_vs_tracked(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        term: str | None = None,
    ) -> SyncPage[PlannedVsTrackedEntry]:
        """Retrieve the planned vs tracked report."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if term is not None:
            params["term"] = term
        return self._get_list(
            "/report/planned_vs_tracked",
            params=params,
            cast_to=PlannedVsTrackedEntry,
        )

    def utilization(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> SyncPage[UtilizationEntry]:
        """Retrieve the utilization report."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        return self._get_list(
            "/report/utilization", params=params, cast_to=UtilizationEntry
        )


class AsyncReports(AsyncResource):
    """Asynchronous reports resource."""

    async def absences(
        self,
        *,
        active: bool | None = None,
        year: int | None = None,
    ) -> AsyncPage[AbsenceEntry]:
        """Retrieve the absences report."""
        params: dict[str, Any] = {}
        if active is not None:
            params["active"] = active
        if year is not None:
            params["year"] = year
        return await self._get_list(
            "/report/absences", params=params, cast_to=AbsenceEntry
        )

    async def cashflow(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        term: str | None = None,
    ) -> AsyncPage[CashflowEntry]:
        """Retrieve the cashflow report."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if term is not None:
            params["term"] = term
        return await self._get_list(
            "/report/cashflow", params=params, cast_to=CashflowEntry
        )

    async def finance(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        term: str | None = None,
    ) -> AsyncPage[FinanceEntry]:
        """Retrieve the finance report."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if term is not None:
            params["term"] = term
        return await self._get_list(
            "/report/finance", params=params, cast_to=FinanceEntry
        )

    async def planned_vs_tracked(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        term: str | None = None,
    ) -> AsyncPage[PlannedVsTrackedEntry]:
        """Retrieve the planned vs tracked report."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if term is not None:
            params["term"] = term
        return await self._get_list(
            "/report/planned_vs_tracked",
            params=params,
            cast_to=PlannedVsTrackedEntry,
        )

    async def utilization(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> AsyncPage[UtilizationEntry]:
        """Retrieve the utilization report."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        return await self._get_list(
            "/report/utilization", params=params, cast_to=UtilizationEntry
        )
