import json


def export_records_json(rows: list[dict]) -> str:
    return json.dumps(rows, indent=2)
