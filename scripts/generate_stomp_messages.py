"""Generate the STOMP message types shipped in ``waldur_api_client.stomp_messages``.

Mastermind describes the messages it publishes to event consumers (site agents
and other integrations subscribed over Web-STOMP) as an AsyncAPI 3.0 document,
generated from ``marketplace_site_agent/contracts.py``. Its "Generate OpenAPI
schema" job publishes it next to the OpenAPI schema as ``waldur-asyncapi.yaml``,
so this client carries both halves of the contract from the same commit.

Usage:
    python scripts/generate_stomp_messages.py waldur-asyncapi.yaml waldur_api_client/stomp_messages.py
    python scripts/generate_stomp_messages.py waldur-asyncapi.yaml waldur_api_client/stomp_messages.py --check
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

HEADER = '''"""Types of the STOMP messages Waldur publishes to event consumers.

Generated from mastermind's AsyncAPI document ({title} {version}, AsyncAPI {asyncapi}),
shipped next to this module as ``asyncapi.yaml``. Do not edit by hand: the
client's pipeline regenerates it with scripts/generate_stomp_messages.py.

Each message has a TypedDict named after it. Required keys live in a private
base class and optional keys in a ``total=False`` subclass (``NotRequired``
needs Python 3.11). An object type that carries several messages also has a
merged ``<ObjectType>Event`` TypedDict: a handler subscribed to the type can
receive any of them, so only keys every message carries are required.
"""

# Optional/Union instead of PEP 604 `X | Y` keeps typing.get_type_hints() working on Python 3.9.
# ruff: noqa: UP007, UP045
from typing import Any, Literal, Optional, TypedDict, Union  # noqa: F401
'''


ENVELOPE_REF = "#/components/schemas/Envelope"

PRIMITIVE_TYPES = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "object": "dict[str, Any]",
}


@dataclass(frozen=True)
class TypeSpec:
    """Structured representation of a generated Python field annotation."""

    enum_values: tuple[Any, ...] | None
    base_type: str
    nullable: bool

    def core_annotation(self) -> str:
        if self.enum_values is not None:
            return _literal(list(self.enum_values))
        return self.base_type

    def render(self) -> str:
        core = self.core_annotation()
        return f"Optional[{core}]" if self.nullable else core


@dataclass(frozen=True)
class Field:
    """One field of a message TypedDict."""

    name: str
    type_spec: TypeSpec
    required: bool


def _literal(values: list[Any]) -> str:
    return "Literal[{}]".format(", ".join(json.dumps(v) for v in values))


def schema_to_type(schema: dict[str, Any]) -> TypeSpec:
    """Convert one JSON Schema property into a ``TypeSpec``."""
    raw_type = schema["type"]
    types = raw_type if isinstance(raw_type, list) else [raw_type]
    nullable = "null" in types
    non_null_types = [t for t in types if t != "null"]
    if len(non_null_types) != 1:
        raise ValueError(f"Expected exactly one non-null JSON type, got {types!r}")
    (json_type,) = non_null_types

    if "enum" in schema:
        raw_enum = schema["enum"]
        nullable = nullable or any(v is None for v in raw_enum)
        values = tuple(v for v in raw_enum if v is not None)
        if values:
            return TypeSpec(enum_values=values, base_type="", nullable=nullable)
        return TypeSpec(enum_values=None, base_type="None", nullable=False)

    if json_type == "array":
        items = schema.get("items")
        item_annotation = schema_to_type(items).render() if items else "Any"
        return TypeSpec(enum_values=None, base_type=f"list[{item_annotation}]", nullable=nullable)

    return TypeSpec(enum_values=None, base_type=PRIMITIVE_TYPES[json_type], nullable=nullable)


def python_type(schema: dict[str, Any]) -> str:
    """The Python 3.9-compatible annotation string for one property schema."""
    return schema_to_type(schema).render()


def message_fields(document: dict[str, Any], message: dict[str, Any]) -> list[Field]:
    """Envelope fields then the message's own, the message's winning on a clash."""
    parts = message["payload"]["allOf"]
    envelope = document["components"]["schemas"]["Envelope"]
    assert parts[0] == {"$ref": ENVELOPE_REF}, "payload must start with the envelope"
    fields: dict[str, Field] = {}
    for schema in (envelope, parts[1]):
        required = set(schema.get("required", []))
        for name, prop in schema["properties"].items():
            # allOf: a key either part requires is required.
            already_required = name in fields and fields[name].required
            fields[name] = Field(
                name=name,
                type_spec=schema_to_type(prop),
                required=already_required or name in required,
            )
    return list(fields.values())


def merge_type_specs(specs: list[TypeSpec]) -> TypeSpec:
    """Merge the type annotations of a field across several message variants."""
    nullable = any(spec.nullable for spec in specs)
    if all(spec.enum_values is not None for spec in specs):
        values: list[Any] = []
        for spec in specs:
            for value in spec.enum_values or ():
                if value not in values:
                    values.append(value)
        return TypeSpec(enum_values=tuple(values), base_type="", nullable=nullable)

    cores: list[str] = []
    for spec in specs:
        core = spec.core_annotation()
        if core not in cores:
            cores.append(core)
    base = cores[0] if len(cores) == 1 else f"Union[{', '.join(cores)}]"
    return TypeSpec(enum_values=None, base_type=base, nullable=nullable)


def merge_fields(variants: list[list[Field]]) -> list[Field]:
    """Fields of a handler that receives any of ``variants``."""
    order: list[str] = []
    specs_by_name: dict[str, list[TypeSpec]] = {}
    required_in: dict[str, int] = {}
    for fields in variants:
        for field in fields:
            if field.name not in specs_by_name:
                order.append(field.name)
                specs_by_name[field.name] = []
                required_in[field.name] = 0
            if field.type_spec not in specs_by_name[field.name]:
                specs_by_name[field.name].append(field.type_spec)
            required_in[field.name] += field.required
    return [
        Field(
            name=name,
            type_spec=merge_type_specs(specs_by_name[name]),
            required=required_in[name] == len(variants),
        )
        for name in order
    ]


def _escape_docstring(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')


def render_typed_dict(name: str, fields: list[Field], docstring: str) -> str:
    required = [f for f in fields if f.required]
    optional = [f for f in fields if not f.required]
    base = f"_{name}Required"
    lines = [f"class {base}(TypedDict):", f'    """Required keys of {name}."""', ""]
    lines += [f"    {f.name}: {f.type_spec.render()}" for f in required]
    lines += ["", ""]
    lines += [f"class {name}({base}, total=False):"]
    lines += [f'    """{_escape_docstring(docstring)}"""', ""] if docstring else []
    lines += [f"    {f.name}: {f.type_spec.render()}" for f in optional]
    if not optional and not docstring:
        lines.append("    pass")
    return "\n".join(lines).rstrip() + "\n"


def event_name(object_type: str) -> str:
    return "".join(part.capitalize() for part in object_type.split("_")) + "Event"


def generate(document: dict[str, Any]) -> str:
    messages = document["components"]["messages"]
    blocks = [HEADER.format(**document["info"], asyncapi=document["asyncapi"])]
    fields_by_message = {}
    for name, message in messages.items():
        fields = message_fields(document, message)
        fields_by_message[name] = fields
        summary = " ".join(message.get("summary", "").split())
        blocks.append(render_typed_dict(name, fields, summary))

    by_type: dict[str, list[str]] = {}
    for name, message in messages.items():
        for object_type in message["x-waldur-object-types"]:
            by_type.setdefault(object_type, []).append(name)
    for object_type, names in by_type.items():
        if len(names) < 2:
            continue
        merged = merge_fields([fields_by_message[n] for n in names])
        docstring = f"Any message delivered for {object_type}: {', '.join(names)}."
        blocks.append(render_typed_dict(event_name(object_type), merged, docstring))

    lines = [
        "",
        "# Message names by the object type they are delivered for.",
        "MESSAGES_BY_OBJECT_TYPE: dict[str, tuple[str, ...]] = {",
    ]
    lines += [
        f"    {json.dumps(object_type)}: ({', '.join(json.dumps(n) for n in names)},),"
        for object_type, names in by_type.items()
    ]
    lines += ["}"]
    blocks.append("\n".join(lines) + "\n")
    return "\n\n\n".join(block.rstrip("\n") for block in blocks) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("document", type=Path, help="the AsyncAPI document (waldur-asyncapi.yaml)")
    parser.add_argument("output", type=Path, help="the module to write")
    parser.add_argument("--check", action="store_true", help="fail when the module is out of date")
    args = parser.parse_args()

    generated = generate(yaml.safe_load(args.document.read_text()))
    if args.check:
        if not args.output.exists() or args.output.read_text() != generated:
            print(f"{args.output} is out of date with {args.document}.")
            return 1
        return 0
    args.output.write_text(generated)
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
