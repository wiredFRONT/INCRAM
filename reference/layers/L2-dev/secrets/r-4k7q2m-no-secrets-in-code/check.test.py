#!/usr/bin/env python3
"""Tests for check.py. Run: python3 check.test.py"""
import importlib.util
import pathlib
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("check", HERE / "check.py")
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


def scan_text(name, text):
    with tempfile.TemporaryDirectory() as folder:
        (pathlib.Path(folder) / name).write_text(text, encoding="utf-8")
        return check.scan(folder)


class Fixtures(unittest.TestCase):
    def test_pass_fixtures_have_no_findings(self):
        self.assertEqual(check.scan(HERE / "fixtures" / "pass"), [])

    def test_fail_fixtures_fail(self):
        findings = check.scan(HERE / "fixtures" / "fail")
        self.assertEqual(check.result(findings), "fail")
        self.assertEqual({rel for _, rel, *_ in findings}, {"deploy.sh", "id_key.pem", "settings.py", ".env"})


class Patterns(unittest.TestCase):
    # Values are assembled here so no real-looking key sits in the repository.
    def test_source_control_token(self):
        self.assertEqual(check.result(scan_text("a.txt", "t = gh" + "p_" + "a" * 36)), "fail")

    def test_live_payment_key(self):
        self.assertEqual(check.result(scan_text("a.js", "const k = 's" + "k_live_" + "b" * 24 + "'")), "fail")

    def test_placeholder_is_not_a_finding(self):
        self.assertEqual(scan_text("a.py", 'API_KEY = "<your-key-here>"'), [])

    def test_reading_from_environment_is_not_a_finding(self):
        self.assertEqual(scan_text("a.py", 'API_KEY = os.environ["API_KEY"]'), [])

    def test_assigned_value_needs_a_person(self):
        self.assertEqual(check.result(scan_text("a.py", 'db_password = "correct-horse-battery"')), "review")

    def test_sample_env_file_is_ignored_for_plain_values(self):
        self.assertEqual(scan_text(".env.example", "API_TOKEN=abc123def456"), [])

    def test_secret_is_never_in_the_output(self):
        secret = "correct-horse-battery"
        findings = scan_text("a.py", f'db_password = "{secret}"')
        self.assertNotIn(secret, repr(findings))


if __name__ == "__main__":
    unittest.main()
