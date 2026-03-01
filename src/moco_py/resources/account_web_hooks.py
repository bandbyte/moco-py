"""Account Web Hooks resource."""

from __future__ import annotations

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import WebhookEvent, WebhookTarget
from ..types.account_web_hooks import WebHook


class AccountWebHooks(SyncResource):
    """Synchronous account web hooks resource."""

    def list(self) -> SyncPage[WebHook]:
        """Retrieve all web hooks."""
        return self._get_list("/account/web_hooks", cast_to=WebHook)

    def get(self, web_hook_id: int) -> MocoResponse[WebHook]:
        """Retrieve a single web hook."""
        return self._get(f"/account/web_hooks/{web_hook_id}", cast_to=WebHook)

    def create(self, *, target: WebhookTarget, event: WebhookEvent, hook: str) -> MocoResponse[WebHook]:
        """Create a web hook."""
        return self._post(
            "/account/web_hooks",
            json_data={"target": target, "event": event, "hook": hook},
            cast_to=WebHook,
        )

    def update(self, web_hook_id: int, *, hook: str) -> MocoResponse[WebHook]:
        """Update a web hook."""
        return self._put(
            f"/account/web_hooks/{web_hook_id}",
            json_data={"hook": hook},
            cast_to=WebHook,
        )

    def disable(self, web_hook_id: int) -> MocoResponse[WebHook]:
        """Disable a web hook."""
        return self._put(
            f"/account/web_hooks/{web_hook_id}/disable",
            json_data={},
            cast_to=WebHook,
        )

    def enable(self, web_hook_id: int) -> MocoResponse[WebHook]:
        """Enable a web hook."""
        return self._put(
            f"/account/web_hooks/{web_hook_id}/enable",
            json_data={},
            cast_to=WebHook,
        )

    def delete(self, web_hook_id: int) -> MocoResponse[None]:
        """Delete a web hook."""
        return self._delete(f"/account/web_hooks/{web_hook_id}")


class AsyncAccountWebHooks(AsyncResource):
    """Asynchronous account web hooks resource."""

    async def list(self) -> AsyncPage[WebHook]:
        """Retrieve all web hooks."""
        return await self._get_list("/account/web_hooks", cast_to=WebHook)

    async def get(self, web_hook_id: int) -> MocoResponse[WebHook]:
        """Retrieve a single web hook."""
        return await self._get(f"/account/web_hooks/{web_hook_id}", cast_to=WebHook)

    async def create(
        self, *, target: WebhookTarget, event: WebhookEvent, hook: str
    ) -> MocoResponse[WebHook]:
        """Create a web hook."""
        return await self._post(
            "/account/web_hooks",
            json_data={"target": target, "event": event, "hook": hook},
            cast_to=WebHook,
        )

    async def update(self, web_hook_id: int, *, hook: str) -> MocoResponse[WebHook]:
        """Update a web hook."""
        return await self._put(
            f"/account/web_hooks/{web_hook_id}",
            json_data={"hook": hook},
            cast_to=WebHook,
        )

    async def disable(self, web_hook_id: int) -> MocoResponse[WebHook]:
        """Disable a web hook."""
        return await self._put(
            f"/account/web_hooks/{web_hook_id}/disable",
            json_data={},
            cast_to=WebHook,
        )

    async def enable(self, web_hook_id: int) -> MocoResponse[WebHook]:
        """Enable a web hook."""
        return await self._put(
            f"/account/web_hooks/{web_hook_id}/enable",
            json_data={},
            cast_to=WebHook,
        )

    async def delete(self, web_hook_id: int) -> MocoResponse[None]:
        """Delete a web hook."""
        return await self._delete(f"/account/web_hooks/{web_hook_id}")
