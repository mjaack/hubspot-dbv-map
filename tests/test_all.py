"""Tests for the map builder and the scanner.

The product here is accuracy: a mapping table that is wrong is worse than no
mapping table. These cover the three mistakes the first cut actually made —
matching paths in place instead of on the version-free skeleton, treating an
OpenAPI `security` alternatives list as a requirements list, and calling a
response-side addition a breaking change.
"""
import json, os, sys, tempfile, unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import build_map
import scan


class TestNormalise(unittest.TestCase):
    def test_version_stripped_wherever_it_sits(self):
        self.assertEqual(build_map.normalize_path("/crm/v3/objects/contacts"),
                         "/crm/objects/contacts")
        self.assertEqual(build_map.normalize_path("/crm/objects/2026-09/contacts"),
                         "/crm/objects/contacts")

    def test_legacy_and_dbv_paths_normalise_together(self):
        self.assertEqual(build_map.normalize_path("/crm/v3/objects/contacts"),
                         build_map.normalize_path("/crm/objects/2026-09/contacts"))

    def test_only_first_version_segment_is_stripped(self):
        # a literal segment that merely looks like a version further down stays
        self.assertEqual(build_map.normalize_path("/a/v3/b/v3/c"), "/a/b/v3/c")

    def test_version_moved_detects_a_change_of_position(self):
        self.assertTrue(build_map.version_moved("/crm/v3/objects/contacts",
                                                "/crm/objects/2026-09/contacts"))
        self.assertFalse(build_map.version_moved("/account-info/v3/details",
                                                 "/account-info/2026-09/details"))


class TestDiffDirection(unittest.TestCase):
    def test_new_required_request_field_breaks_the_caller(self):
        old = {"a": {"type": "string", "required": False}}
        new = {"a": {"type": "string", "required": True}}
        c = build_map.diff_fields(old, new, "request field")
        self.assertTrue(c[0]["breaking"])

    def test_new_required_response_field_does_not(self):
        old = {"a": {"type": "string", "required": False}}
        new = {"a": {"type": "string", "required": True}}
        c = build_map.diff_fields(old, new, "response field", response=True)
        self.assertFalse(c[0]["breaking"])

    def test_removed_field_breaks_in_both_directions(self):
        old = {"a": {"type": "string"}}
        for response in (True, False):
            c = build_map.diff_fields(old, {}, "field", response=response)
            self.assertEqual(c[0]["change"], "removed")
            self.assertTrue(c[0]["breaking"])

    def test_type_change_is_breaking(self):
        c = build_map.diff_fields({"a": {"type": "string"}}, {"a": {"type": "array"}}, "request field")
        self.assertTrue(any(x["change"] == "type_changed" and x["breaking"] for x in c))

    def test_enum_value_removal_is_breaking_but_addition_is_not(self):
        c = build_map.diff_fields({"a": {"enum": ["X", "Y"]}}, {"a": {"enum": ["X"]}}, "request field")
        self.assertTrue(c[0]["breaking"])
        c = build_map.diff_fields({"a": {"enum": ["X"]}}, {"a": {"enum": ["X", "Y"]}}, "request field")
        self.assertFalse(c[0]["breaking"])


class TestScopes(unittest.TestCase):
    def test_security_is_a_list_of_alternatives(self):
        op = {"security": [{"oauth2": ["a"]}, {"oauth2": ["b"]}, {"private_apps": ["c"]}]}
        self.assertEqual(build_map.scopes(op), ["a", "b", "c"])

    def test_no_security_block_yields_nothing(self):
        self.assertEqual(build_map.scopes({}), [])


class TestSchemaFlattening(unittest.TestCase):
    def test_refs_are_resolved(self):
        spec = {"components": {"schemas": {"Thing": {
            "type": "object", "required": ["id"],
            "properties": {"id": {"type": "string"}, "n": {"type": "integer"}}}}}}
        flat = build_map.flatten(spec, {"$ref": "#/components/schemas/Thing"})
        self.assertEqual(flat["id"]["type"], "string")
        self.assertTrue(flat["id"]["required"])
        self.assertFalse(flat["n"]["required"])

    def test_recursive_refs_terminate(self):
        spec = {"components": {"schemas": {"Node": {
            "type": "object",
            "properties": {"child": {"$ref": "#/components/schemas/Node"}}}}}}
        flat = build_map.flatten(spec, {"$ref": "#/components/schemas/Node"})
        self.assertIn("child", flat)

    def test_arrays_are_flattened_with_a_marker(self):
        spec = {}
        flat = build_map.flatten(spec, {
            "type": "object",
            "properties": {"inputs": {"type": "array", "items": {
                "type": "object", "properties": {"id": {"type": "string"}}}}}})
        self.assertIn("inputs[].id", flat)


class TestScanner(unittest.TestCase):
    def test_skeleton_drops_version_and_ids(self):
        self.assertEqual(scan.skeleton("/crm/v3/objects/contacts/12345"),
                         "/crm/objects/contacts/*")
        self.assertEqual(scan.skeleton("/crm/v3/objects/contacts/{contactId}"),
                         "/crm/objects/contacts/*")
        self.assertEqual(scan.skeleton("/crm/v3/objects/contacts?limit=10"),
                         "/crm/objects/contacts")

    def test_finds_a_real_legacy_call_and_maps_it(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "a.js"), "w").write(
                'const r = await fetch("https://api.hubapi.com/crm/v3/objects/contacts");\n')
            _m, findings, _o = scan.scan(d)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0]["op"]["method"], "GET")
            self.assertTrue(findings[0]["op"]["target_path"].startswith("/crm/objects/"))

    def test_flags_legacy_auth_and_sdk(self):
        with tempfile.TemporaryDirectory() as d:
            # assembled at runtime so the fixture is not itself mistaken for a
            # leaked credential by secret scanners
            fake_token = "pat-" + "na1-" + "0a1b2c3d-4e5f-6789-abcd-ef0123456789"
            with open(os.path.join(d, "b.py"), "w") as fh:
                fh.write(f'TOKEN = "{fake_token}"\n'
                         'URL = "https://api.hubapi.com/contacts/v1/lists/all?hapikey=x"\n')
            _m, _f, other = scan.scan(d)
            kinds = {o["kind"] for o in other}
            self.assertIn("legacy_private_app_token", kinds)
            self.assertIn("hapikey", kinds)

    def test_matches_concrete_values_against_path_templates(self):
        # the call site writes `contacts/deals`, the spec writes
        # `{fromObjectType}/{toObjectType}`
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "a.js"), "w") as fh:
                fh.write('fetch("https://api.hubapi.com/crm/v3/associations/contacts/deals/'
                         'batch/create", {method:"POST"})\n')
            _m, findings, _o = scan.scan(d)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0]["op"]["method"], "POST")
            self.assertTrue(findings[0]["op"]["breaking"])

    def test_detects_the_verb(self):
        for line, want in [('fetch(url, {method: "POST"})', "POST"),
                           ('requests.delete(url)', "DELETE"),
                           ('await client.patch(url)', "PATCH"),
                           ('curl -X PUT https://api.hubapi.com/x', "PUT"),
                           ('const x = 1', None)]:
            self.assertEqual(scan.detect_method(line), want, line)

    def test_unknown_verb_reports_the_worst_candidate(self):
        # a bare URL with no verb must not be reported as the clean GET when a
        # sibling method on the same path has no replacement
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "a.txt"), "w") as fh:
                fh.write("https://api.hubapi.com/integrators/timeline/v3/9/event-templates\n")
            _m, findings, _o = scan.scan(d)
            self.assertEqual(findings[0]["op"]["status"], "REMOVED")
            self.assertFalse(findings[0]["method_detected"])

    def test_ignores_unrelated_versioned_paths(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "c.js"), "w").write('fetch("https://example.com/api/v3/widgets")\n')
            _m, findings, _o = scan.scan(d)
            self.assertEqual(findings, [])

    def test_skips_node_modules(self):
        with tempfile.TemporaryDirectory() as d:
            nm = os.path.join(d, "node_modules")
            os.makedirs(nm)
            open(os.path.join(nm, "x.js"), "w").write(
                'fetch("https://api.hubapi.com/crm/v3/objects/contacts")\n')
            _m, findings, _o = scan.scan(d)
            self.assertEqual(findings, [])


class TestBuiltMap(unittest.TestCase):
    """Sanity checks on the shipped artefact itself."""

    @classmethod
    def setUpClass(cls):
        p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "map.json")
        cls.m = json.load(open(p))

    def test_every_operation_has_a_verdict(self):
        allowed = {"IDENTICAL", "CHANGED", "BREAKING", "MOVED", "REMOVED", "NO_DBV_VERSION"}
        for o in self.m["operations"]:
            self.assertIn(o["status"], allowed)

    def test_mapped_operations_carry_a_target(self):
        for o in self.m["operations"]:
            if o["status"] in ("REMOVED", "NO_DBV_VERSION"):
                self.assertIsNone(o["target_path"])
            else:
                self.assertTrue(o["target_path"])

    def test_no_scope_addition_claims_survive(self):
        # the first cut reported ~328 of these and every one was wrong
        for o in self.m["operations"]:
            for c in o["changes"]:
                self.assertNotEqual(c["change"], "scope_added")

    def test_path_move_is_not_claimed_as_breaking(self):
        # both shapes still route as of 2026-09-17; verified live
        for o in self.m["operations"]:
            for c in o["changes"]:
                if c["change"] == "version_segment_moved":
                    self.assertFalse(c["breaking"])

    def test_contacts_maps_to_the_restructured_path(self):
        hit = [o for o in self.m["operations"]
               if o["legacy_path"] == "/crm/v3/objects/contacts" and o["method"] == "GET"]
        self.assertTrue(hit)
        self.assertTrue(hit[0]["target_path"].startswith("/crm/objects/"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
