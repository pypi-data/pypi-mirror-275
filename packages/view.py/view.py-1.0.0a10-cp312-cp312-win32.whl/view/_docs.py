from __future__ import annotations

from typing import TYPE_CHECKING, Any, get_args

from typing_extensions import get_origin

from .typing import DocsType

if TYPE_CHECKING:
    from ._loader import LoaderDoc
    from .app import InputDoc
    from .routing import _NoDefaultType

_PRIMITIVES = {
    str: "string",
    int: "integer",
    dict: "object",
    Any: "any",
    bool: "boolean",
    float: "double",
    None: "null",
}


def _tp_name(tp: Any, types: list[Any]) -> str:
    prim = _PRIMITIVES.get(tp)
    if prim:
        return f"`{prim}`"
    else:
        if tp not in types:
            doc: dict[str, LoaderDoc] | None = getattr(tp, "_view_doc", None)
            if not doc:
                if hasattr(tp, "__origin__"):
                    origin = get_origin(tp)
                    args = get_args(tp)
                    tp_name = _PRIMITIVES.get(origin) or getattr(
                        origin, "__name__", str(origin)
                    )
                    parsed_args = [(_PRIMITIVES.get(i) or i.__name__) for i in args]
                    return f"`{tp_name}<{', '.join(parsed_args)}>`"

                return f"`{doc}`"

            types.append(tp)

            for v in doc.values():
                _tp_name(v.tp, types)

        return f"`{tp.__name__}`"


def _format_type(tp: tuple[type[Any], ...], types: list[Any]) -> str:
    if len(tp) == 1:
        return _tp_name(tp[0], types)

    final = ""

    for index, i in enumerate(tp):
        if (index + 1) == len(tp):
            final += _tp_name(i, types)
        else:
            final += f"{_tp_name(i, types)} | "

    return final


def _format_default(default: Any | _NoDefaultType) -> str:
    if hasattr(default, "__VIEW_NODEFAULT__"):
        return "**Required**"

    return f"`{default!r}`"


def _make_table(
    final: list[str],
    table_name: str,
    inputs: dict[str, InputDoc],
    types: list[Any],
) -> None:
    if not inputs:
        return

    final.append(f"#### {table_name}")
    final.append("| Name | Description | Type | Default |")
    final.append("| - | - | - | - |")

    for name, body in inputs.items():
        final.append(
            f"| {name} | {body.desc} | {_format_type(body.type, types)} | {_format_default(body.default)} |"  # noqa
        )


def markdown_docs(docs: DocsType) -> str:
    final: list[str] = []
    types: list[Any] = []
    if docs:
        final.append(f"\n## Routes")
    else:
        final.append("\n*This app is empty...*")

    for k, v in docs.items():
        name = k[0] if isinstance(k[0], str) else ", ".join(k[0])
        final.append(f"### {name} `{k[1]}`")
        final.append(f"*{v.desc}*")

        _make_table(final, "Query Parameters", v.query, types)
        _make_table(final, "Body Parameters", v.body, types)

    part = ["\n## Types"] if types else [""]

    for i in types:
        doc: dict[str, LoaderDoc] = getattr(i, "_view_doc")
        part.append(f"### `{i.__name__}`")
        part.append("| Key | Description | Type | Default |")
        part.append("| - | - | - | - |")

        for name, loader_doc in doc.items():
            part.append(
                f"| {name} | {loader_doc.desc} | {_format_type((loader_doc.tp,), types)} | {_format_default(loader_doc.default)} |"  # noqa
            )

    return "# Docs" + "\n".join(part) + "\n".join(final)
