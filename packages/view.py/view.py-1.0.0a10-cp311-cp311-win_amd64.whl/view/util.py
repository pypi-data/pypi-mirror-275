from __future__ import annotations

import json
import logging
import os
from datetime import datetime as DateTime
from email.utils import formatdate
from typing import TYPE_CHECKING, Union, overload

from ._logging import Internal, Service
from ._util import run_path, shell_hint
from .exceptions import AppNotFoundError, BadEnvironmentError, MistakeError

if TYPE_CHECKING:
    from .app import App

__all__ = ("run", "env", "enable_debug", "timestamp", "extract_path")


def extract_path(path: str) -> App:
    """Extract an `App` instance from a path."""
    from .app import App

    split = path.split(":", maxsplit=1)

    if len(split) != 2:
        raise ValueError(
            "module string should be in the format of `/path/to/app.py:app_name`",
        )

    file_path = os.path.abspath(split[0])

    try:
        mod = run_path(file_path)
    except FileNotFoundError:
        raise AppNotFoundError(f'"{split[0]}" in {path} does not exist') from None

    try:
        target = mod[split[1]]
    except KeyError:
        raise AttributeError(f'"{split[1]}" in {path} does not exist') from None

    if not isinstance(target, App):
        raise MistakeError(f"{target!r} is not an instance of view.App")

    return target


def run(app_or_path: str | App) -> None:
    """Run a view app. Should not be used over `App.run()`
        middleware: list[__Middleware],

    Args:
        app_or_path: App object or path to run."""
    from .app import App

    if isinstance(app_or_path, App):
        app_or_path.run()
        return

    target = extract_path(app_or_path)
    target._run()


def enable_debug():
    """Enable debug mode."""
    internal = Internal.log
    internal.disabled = False
    internal.setLevel(logging.DEBUG)
    internal.addHandler(
        logging.StreamHandler(open("view_internal.log", "w", encoding="utf-8"))
    )
    Service.log.addHandler(
        logging.StreamHandler(open("view_service.log", "w", encoding="utf-8"))
    )

    Internal.info("debug mode enabled")
    os.environ["VIEW_DEBUG"] = "1"


EnvConv = Union[str, int, bool, dict]

# good god why does mypy suck at the very thing it's designed to do

@overload
def env(key: str, *, tp: type[str] = str) -> str:  # type: ignore
    ...


@overload
def env(key: str, *, tp: type[int] = int) -> int:  # type: ignore
    ...


@overload
def env(key: str, *, tp: type[bool] = bool) -> bool:  # type: ignore
    ...


@overload
def env(key: str, *, tp: type[dict] = dict) -> dict:  # type: ignore
    ...


def env(key: str, *, tp: type[EnvConv] = str) -> EnvConv:
    """Get and parse an environment variable.

    Args:
        key: Environment variable to access.
        tp: Type to convert to.

    Example:
        ```py
        from view import new_app, env

        app = new_app()

        @app.get("/")
        def index():
            return env("FOO")

        app.run()
        ```
    """
    value = os.environ.get(key)

    if not value:
        raise BadEnvironmentError(
            f'environment variable "{key}" not set',
            hint=shell_hint(
                f"set {key}=..." if os.name == "nt" else f"export {key}=..."
            ),
        )

    if tp is str:
        return value

    if tp is int:
        try:
            return int(value)
        except ValueError:
            raise BadEnvironmentError(f"{value!r} (key {key!r}) is not int-like") from None

    if tp is dict:
        try:
            return json.loads(value)
        except ValueError:
            raise BadEnvironmentError(f"{value!r} ({key!r}) is not dict-like")

    if tp is bool:
        value = value.lower()
        if value not in {"true", "false"}:
            raise BadEnvironmentError(f"{value!r} ({key!r}) is not bool-like")

        return value == "true"

    raise ValueError(f"{tp.__name__} cannot be converted")


_Now = None


def timestamp(tm: DateTime | None = _Now) -> str:
    """RFC 1123 Compliant Timestamp

    Args:
        tm: Date object to create a timestamp for. Now by default."""
    stamp: float = DateTime.now().timestamp() if not tm else tm.timestamp()
    return formatdate(stamp, usegmt=True)
