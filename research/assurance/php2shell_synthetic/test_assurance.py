import unittest
from assurance import assess,dashboard_fixture
class AssuranceTests(unittest.TestCase):
    def test_fixture(self):
        self.assertEqual(len(dashboard_fixture()["records"]),2)
        self.assertFalse(dashboard_fixture()["actual_cve_exploit_reproduced"])
    def test_missing_patch(self):
        with self.assertRaises(ValueError): assess({"case_id":"x","status":"remediated"})
    def test_missing_reviewer(self):
        with self.assertRaises(ValueError): assess({"case_id":"x","status":"independently_verified","patch_evidence":"p","regression_passed":True})
    def test_invalid_state(self):
        with self.assertRaises(ValueError): assess({"case_id":"x","status":"secure"})
    def test_reported(self):
        self.assertFalse(assess({"case_id":"x","status":"reported"})["evidence_complete"])
if __name__=="__main__": unittest.main()
