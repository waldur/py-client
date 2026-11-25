"""Unit tests for scripts/generate_stomp_messages.py and waldur_api_client.stomp_messages."""

import ast
import importlib.util
import sys
import typing
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import generate_stomp_messages as gen  # noqa: E402

ASYNCAPI_PATH = ROOT / "waldur_api_client" / "asyncapi.yaml"
MODULE_PATH = ROOT / "waldur_api_client" / "stomp_messages.py"


def _load_module_from_source(source: str, name: str = "_generated_stomp_messages"):
    namespace: dict[str, object] = {}
    exec(compile(source, f"<{name}>", "exec"), namespace)
    return namespace


class GenerateStompMessagesTest(unittest.TestCase):
    def test_committed_module_is_current(self):
        document = yaml.safe_load(ASYNCAPI_PATH.read_text())
        self.assertEqual(
            MODULE_PATH.read_text(),
            gen.generate(document),
            "waldur_api_client/stomp_messages.py is out of date with waldur_api_client/asyncapi.yaml",
        )

    def test_committed_module_parses_as_python_3_9(self):
        ast.parse(MODULE_PATH.read_text(), feature_version=(3, 9))

    def test_committed_module_imports_and_resolves_type_hints(self):
        mod_name = "stomp_messages_under_test"
        spec = importlib.util.spec_from_file_location(mod_name, MODULE_PATH)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[mod_name] = module
        try:
            spec.loader.exec_module(module)

            document = yaml.safe_load(ASYNCAPI_PATH.read_text())
            envelope_required = set(document["components"]["schemas"]["Envelope"].get("required", []))
            for name, message in document["components"]["messages"].items():
                typed = getattr(module, name)
                hints = typing.get_type_hints(typed)
                body = message["payload"]["allOf"][1]
                expected_required = envelope_required | set(body.get("required", []))
                self.assertEqual(typed.__required_keys__, expected_required, name)
                self.assertTrue(set(body["properties"]) <= set(hints), name)

            for object_type, names in module.MESSAGES_BY_OBJECT_TYPE.items():
                if len(names) >= 2:
                    event_cls = getattr(module, gen.event_name(object_type))
                    typing.get_type_hints(event_cls)

            api_key_doc = module.ApiKeyCommandMessage.__doc__ or ""
            self.assertIn("Attributes:", api_key_doc)
            self.assertIn("allowed_models (optional):", api_key_doc)
            self.assertIn("resource_api_key_rotation", api_key_doc)

            offering_user_event_doc = module.OfferingUserEvent.__doc__ or ""
            self.assertIn("Attributes:", offering_user_event_doc)
            self.assertIn("state (optional):", offering_user_event_doc)
        finally:
            sys.modules.pop(mod_name, None)

    def test_python_type_primitives_and_number(self):
        self.assertEqual(gen.python_type({"type": "string"}), "str")
        self.assertEqual(gen.python_type({"type": "integer"}), "int")
        self.assertEqual(gen.python_type({"type": "number"}), "float")
        self.assertEqual(gen.python_type({"type": "boolean"}), "bool")
        self.assertEqual(gen.python_type({"type": "object"}), "dict[str, Any]")
        self.assertEqual(gen.python_type({"type": ["object", "null"]}), "Optional[dict[str, Any]]")
        self.assertEqual(gen.python_type({"type": "array", "items": {"type": "string"}}), "list[str]")
        self.assertEqual(gen.python_type({"type": "array"}), "list[Any]")

    def test_nullable_enum_filters_none_from_literal(self):
        schema = {"type": ["string", "null"], "enum": ["a", "b", None]}
        self.assertEqual(gen.python_type(schema), 'Optional[Literal["a", "b"]]')

    def test_merge_fields_handles_nullable_enums_and_unions(self):
        v1 = [
            gen.Field("action", gen.schema_to_type({"type": ["string", "null"], "enum": ["a", None]}), True),
            gen.Field("state", gen.schema_to_type({"type": "integer"}), True),
            gen.Field("only_v1", gen.schema_to_type({"type": "number"}), True),
        ]
        v2 = [
            gen.Field("action", gen.schema_to_type({"type": "string", "enum": ["b"]}), True),
            gen.Field("state", gen.schema_to_type({"type": "string"}), False),
        ]
        merged = {f.name: f for f in gen.merge_fields([v1, v2])}
        self.assertEqual(merged["action"].type_spec.render(), 'Optional[Literal["a", "b"]]')
        self.assertTrue(merged["action"].required)
        self.assertEqual(merged["state"].type_spec.render(), "Union[int, str]")
        self.assertFalse(merged["state"].required)
        self.assertEqual(merged["only_v1"].type_spec.render(), "float")
        self.assertFalse(merged["only_v1"].required)

    def test_generated_nullable_enum_and_number_resolve_at_runtime(self):
        document = {
            "asyncapi": "3.0.0",
            "info": {"title": "Test", "version": "1.0.0"},
            "components": {
                "schemas": {
                    "Envelope": {
                        "type": "object",
                        "required": ["object_type"],
                        "properties": {"object_type": {"type": "string"}},
                    }
                },
                "messages": {
                    "FirstMessage": {
                        "summary": 'First """quoted""" summary',
                        "x-waldur-object-types": ["demo"],
                        "payload": {
                            "allOf": [
                                {"$ref": "#/components/schemas/Envelope"},
                                {
                                    "type": "object",
                                    "required": ["status", "ratio"],
                                    "properties": {
                                        "object_type": {"type": "string", "enum": ["demo"]},
                                        "status": {"type": ["string", "null"], "enum": ["ok", None]},
                                        "ratio": {"type": "number"},
                                    },
                                },
                            ]
                        },
                    },
                    "SecondMessage": {
                        "summary": "Second summary",
                        "x-waldur-object-types": ["demo"],
                        "payload": {
                            "allOf": [
                                {"$ref": "#/components/schemas/Envelope"},
                                {
                                    "type": "object",
                                    "required": ["status"],
                                    "properties": {
                                        "object_type": {"type": "string", "enum": ["demo"]},
                                        "status": {"type": "string", "enum": ["erred"]},
                                    },
                                },
                            ]
                        },
                    },
                },
            },
        }
        source = gen.generate(document)
        ast.parse(source, feature_version=(3, 9))
        ns = _load_module_from_source(source)
        self.assertEqual(typing.get_type_hints(ns["FirstMessage"])["ratio"], float)
        self.assertIn("status", typing.get_type_hints(ns["DemoEvent"]))


if __name__ == "__main__":
    unittest.main()
