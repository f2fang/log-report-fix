import json
from pathlib import Path


REPORT = Path("/app/report.json")


def test_success_criterion_1_report_file_exists():
    """Verifies success criterion 1: create /app/report.json as the required output artifact."""
    assert REPORT.exists(), "missing /app/report.json"


def test_success_criterion_2_report_is_exact_json_summary():
    """Verifies success criterion 2: report.json contains exactly total_requests=6, unique_ips=3, and top_path=/index.html."""
    data = json.loads(REPORT.read_text())
    assert data == {
        "total_requests": 6,
        "unique_ips": 3,
        "top_path": "/index.html",
    }
