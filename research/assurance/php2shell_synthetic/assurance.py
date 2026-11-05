"""Offline synthetic PHP remediation assurance. No exploit code or network access."""
import json
CVE_IDS = ("CVE-2026-109618", "CVE-2026-109619")
STATES = {"reported", "reproduced", "remediated", "independently_verified"}
def assess(record):
    state = record["status"]
    if state not in STATES: raise ValueError("unknown status")
    if state in ("remediated", "independently_verified") and not record.get("patch_evidence"): raise ValueError("missing patch evidence")
    if state == "independently_verified" and not (record.get("regression_passed") and record.get("independent_reviewer")): raise ValueError("missing independent review")
    return {"case_id":record["case_id"],"status":state,"synthetic":True,"evidence_complete":state=="independently_verified"}
def dashboard_fixture():
    return {"schema_version":"1.0","case_id":"GRI-PHP2SHELL-2026","cves":list(CVE_IDS),"source":"https://www.wiz.io/blog/php2shell-php-rce","evidence_class":"synthetic_only","actual_cve_exploit_reproduced":False,"production_dashboard_integrated":False,"records":[assess({"case_id":"synthetic-patched","status":"remediated","patch_evidence":"synthetic-build"}),assess({"case_id":"synthetic-unpatched","status":"reported"})]}
if __name__=="__main__": print(json.dumps(dashboard_fixture(),indent=2,sort_keys=True))
