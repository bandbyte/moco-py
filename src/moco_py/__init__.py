"""MOCO ERP API client library."""

from ._pagination import AsyncPage, SyncPage
from ._response import MocoResponse
from .client import AsyncMoco, Moco
from .exceptions import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    MocoError,
    NotFoundError,
    PermissionError,
    RateLimitError,
    ServerError,
    ValidationError,
)

__version__ = "1.1.1"

__all__ = [
    "AsyncMoco",
    "AsyncPage",
    "Moco",
    "MocoResponse",
    "SyncPage",
    "__version__",
    "APIConnectionError",
    "APITimeoutError",
    "AuthenticationError",
    "MocoError",
    "NotFoundError",
    "PermissionError",
    "RateLimitError",
    "ServerError",
    "ValidationError",
]
