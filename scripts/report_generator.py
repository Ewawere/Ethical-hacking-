#!/usr/bin/env python3
import json
from datetime import datetime


def generate_report(scan_results, filename="report.json"):
    report = {
        "generated_at": datetime.utcnow().isoformat(),
        "scope": "local lab only",
        "findings": scan_results
    }

    with open(filename, "w") as f:
        json.dump(report, f, indent=2)

    print(f"Report saved to {filename}")


if __name__ == "__main__":
    sample = [
        {"host": "10.0.2.15", "ports": [22, 80, 443]},
        {"host": "10.0.2.20", "ports": [8080]}
    ]
    generate_report(sample)
