import io

import pandas as pd


def export_records_csv(rows: list[dict]) -> str:
    df = pd.DataFrame(rows)
    out = io.StringIO()
    df.to_csv(out, index=False)
    return out.getvalue()
