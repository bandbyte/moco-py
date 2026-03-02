"""Helpers for converting files to the base64 format expected by the MOCO API."""

from __future__ import annotations

import base64
from os import PathLike
from pathlib import Path
from typing import TypedDict


class FileAttachment(TypedDict):
    """Dict with ``filename`` and ``base64`` keys as expected by the MOCO API."""

    filename: str
    base64: str


def file_to_base64(path: str | PathLike[str]) -> FileAttachment:
    """Read a file from *path* and return a :class:`FileAttachment` dict.

    The returned dict can be passed directly to any MOCO API parameter that
    expects a ``{"filename": "...", "base64": "..."}`` object (e.g. purchase
    ``file``, receipt ``attachment``, invoice/offer attachment, etc.).

    Example::

        from moco_py import Moco, file_to_base64

        client = Moco(domain="company", api_key="...")
        client.invoices.create_attachment(
            invoice_id=123,
            **file_to_base64("invoice-appendix.pdf"),
        )
    """
    p = Path(path)
    data = p.read_bytes()
    return FileAttachment(
        filename=p.name,
        base64=base64.b64encode(data).decode("ascii"),
    )
