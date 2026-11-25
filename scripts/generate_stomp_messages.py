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

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

HEADER = '''\"\"\"Types of the STOMP messages Waldur publishes to event consumers.

Generated from mastermind's AsyncAPI document ({title} {version}, AsyncAPI {asyncapi}),
shipped next to this module as ``asyncapi.yaml``. Do not edit by hand: the
client's pipeline regenerates it with scripts/generate_stomp_messages.py.

Each message has a TypedDict named after it. Required keys live in a private
base class and optional keys in a ``total=False`` subclass (``NotRequired``
needs Python 3.11). An object type that carries several messages also has a
merged ``<ObjectType>Event`` TypedDict: a handler subscribed to the type can
receive any of them, so only keys every message carries are required.
\"\"\"

# Keeps the ``X | None`` annotations unevaluated on Python 3.9.
from __future__ import annotations

from typing import Any, Literal, TypedDict  # noqa: F401
'''


ENVELOPE_REF = "#/components/schemas/Envelope"

PRIMITIVE_TYPES = {
    "string": "str",
    "integer": "int",
    "boolean": "bool",
    "object": "dict[str, Any]",
}



def _literal(values: list[str]) -> str:
    return "Literal[{}]".format(", ".join(json.dumps(v) for v in values))


def python_type(schema: dict[str, Any]) -> str:
    """The annotation for one property schema."""
    types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
    nullable = "null" in types
    (json_type,) = [t for t in types if t != "null"]
    if "enum" in schema:
        annotation = _literal(schema["enum"])
    elif json_type == "array":
        items = schema.get("items")
        annotation = f"list[{python_type(items)}]" if items else "list[Any]"
    else:
        annotation = PRIMITIVE_TYPES[json_type]
    return f"{annotation} | None" if nullable else annotation


Field = tuple[str, str, bool]  # name, annotation, required  # name, annotation, required


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
            already_required = name in fields and fields[name][2]
            fields[name] = (name, python_type(prop), already_required or name in required)
    return list(fields.values())


def merge_fields(variants: list[list[Field]]) -> list[Field]:
    """Fields of a handler that receives any of ``variants``."""
    order: list[str] = []
    annotations: dict[str, list[str]] = {}
    required_in: dict[str, int] = {}
    for fields in variants:
        for name, annotation, required in fields:
            if name not in annotations:
                order.append(name)
                annotations[name] = []
                required_in[name] = 0
            if annotation not in annotations[name]:
                annotations[name].append(annotation)
            required_in[name] += required
    merged = []
    for name in order:
        options = annotations[name]
        literals = [o for o in options if o.startswith("Literal[")]
        if len(literals) == len(options) > 1:
            values: list[str] = []
            for option in options:
                values += [v for v in json.loads(f"[{option[8:-1]}]") if v not in values]
            options = [_literal(values)]
        annotation = " | ".join(options)
        merged.append((name, annotation, required_in[name] == len(variants)))
    return merged


def render_typed_dict(name: str, fields: list[Field], docstring: str) -> str:
    required = [f for f in fields if f[2]]
    optional = [f for f in fields if not f[2]]
    base = f"_{name}Required"
    lines = [f"class {base}(TypedDict):", f'    """Required keys of {name}."""', ""]
    lines += [f"    {field_name}: {annotation}" for field_name, annotation, _ in required]
    lines += ["", ""]
    lines += [f"class {name}({base}, total=False):"]
    lines += [f'    """{docstring}"""', ""] if docstring else []
    lines += [f"    {field_name}: {annotation}" for field_name, annotation, _ in optional]
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

    lines = ["", "# Message names by the object type they are delivered for.", "MESSAGES_BY_OBJECT_TYPE = {"]
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
