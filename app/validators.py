
from dataclasses import dataclass
from pathlib import PurePath
import re


MAX_SOURCE_SIZE = 1_000_000  # 1 MB
MAX_FILENAME_LENGTH = 255


class SourceValidationError(ValueError):
    """Raised when submitted Python source is invalid."""


@dataclass(frozen=True)
class ValidatedSource:
    filename: str
    source: str
    size_bytes: int


def validate_source(
    filename: str,
    content: bytes,
) -> ValidatedSource:
    """Validate Python source bytes without executing them."""

    if not isinstance(filename, str) or not filename:
        raise SourceValidationError("A filename is required.")

    if len(filename) > MAX_FILENAME_LENGTH:
        raise SourceValidationError("Filename is too long.")

    # Accept a plain filename only, not a path supplied by the user.
    if filename != PurePath(filename).name or "/" in filename or "\\" in filename:
        raise SourceValidationError("Path components are not allowed.")

    if filename in {".", ".."} or not re.fullmatch(
        r"[A-Za-z0-9_-][A-Za-z0-9_.-]*\.py",
        filename,
    ):
        raise SourceValidationError("A valid .py filename is required.")

    if not isinstance(content, bytes):
        raise SourceValidationError("Source content must be bytes.")

    size_bytes = len(content)

    if size_bytes > MAX_SOURCE_SIZE:
        raise SourceValidationError("Source file exceeds the 1 MB limit.")

    try:
        source = content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SourceValidationError(
            "Source file must use UTF-8 encoding."
        ) from exc

    return ValidatedSource(
        filename=filename,
        source=source,
        size_bytes=size_bytes,
    )
