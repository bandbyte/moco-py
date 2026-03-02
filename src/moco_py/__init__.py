"""MOCO ERP API client library."""

from ._file import FileAttachment, file_to_base64
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

__version__ = "1.2.0"

__all__ = [
    "AsyncMoco",
    "AsyncPage",
    "FileAttachment",
    "file_to_base64",
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
