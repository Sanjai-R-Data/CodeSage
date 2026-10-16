
import pytest

from app.validators import (
    MAX_SOURCE_SIZE,
    SourceValidationError,
    validate_source,
)


def test_valid_python_source():
    result = validate_source("hello.py", b"print('hello')\n")

    assert result.filename == "hello.py"
    assert result.source == "print('hello')\n"
    assert result.size_bytes == len(b"print('hello')\n")


@pytest.mark.parametrize(
    "filename",
    [
        "",
        "hello.txt",
        "../hello.py",
        "folder/hello.py",
        r"folder\hello.py",
        ".py",
    ],
)
def test_rejects_invalid_filename(filename):
    with pytest.raises(SourceValidationError):
        validate_source(filename, b"x = 1")


def test_rejects_oversized_source():
    content = b"x" * (MAX_SOURCE_SIZE + 1)

    with pytest.raises(SourceValidationError, match="1 MB"):
        validate_source("large.py", content)


def test_rejects_invalid_utf8():
    with pytest.raises(SourceValidationError, match="UTF-8"):
        validate_source("bad.py", b"\xff\xfe")


def test_accepts_empty_source():
    result = validate_source("empty.py", b"")

    assert result.source == ""
    assert result.size_bytes == 0
