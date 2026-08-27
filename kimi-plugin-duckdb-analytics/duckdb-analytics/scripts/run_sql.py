#!/usr/bin/env python3
"""Run a DuckDB SQL query against a local data file (CSV / Parquet / JSON).

Usage:
  python3 scripts/run_sql.py --data data.csv --sql "SELECT * FROM t LIMIT 10"
  python3 scripts/run_sql.py --data data.parquet --describe
  python3 scripts/run_sql.py --sql "SELECT 1+1"

The data file is exposed as a view named `t` (override with --table).
Results print as a Markdown table. Use --csv to print CSV instead.
"""

import argparse
import sys
from pathlib import Path

EXTENSION_LOADERS = {
    ".csv": "read_csv_auto",
    ".tsv": "read_csv_auto",
    ".parquet": "read_parquet",
    ".json": "read_json_auto",
    ".jsonl": "read_json_auto",
    ".ndjson": "read_json_auto",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="DuckDB SQL over local files")
    parser.add_argument("--data", help="Path to CSV/TSV/Parquet/JSON data file")
    parser.add_argument("--sql", help="SQL to execute; data file is view `t`")
    parser.add_argument("--table", default="t", help="View name (default: t)")
    parser.add_argument("--describe", action="store_true",
                        help="Show schema + row count of the data file")
    parser.add_argument("--limit", type=int, default=100,
                        help="Max rows to print (default 100)")
    parser.add_argument("--csv", action="store_true", help="Print CSV instead of Markdown")
    args = parser.parse_args()

    try:
        import duckdb
    except ImportError:
        print("ERROR: duckdb module not available in this Python.", file=sys.stderr)
        return 2

    con = duckdb.connect(database=":memory:")

    if args.data:
        data = Path(args.data)
        if not data.exists():
            print(f"ERROR: file not found: {data}", file=sys.stderr)
            return 2
        loader = EXTENSION_LOADERS.get(data.suffix.lower())
        if not loader:
            print(f"ERROR: unsupported extension {data.suffix}; "
                  f"supported: {', '.join(EXTENSION_LOADERS)}", file=sys.stderr)
            return 2
        safe = str(data).replace("'", "''")
        con.execute(f"CREATE VIEW {args.table} AS SELECT * FROM {loader}('{safe}')")

    if args.describe:
        if not args.data:
            parser.error("--describe requires --data")
        sql = f"DESCRIBE {args.table}"
        print(f"# Schema of {args.data}\n")
    elif args.sql:
        sql = args.sql
    else:
        parser.error("one of --sql or --describe is required")

    try:
        rel = con.sql(sql)
    except Exception as exc:  # DuckDB raises various error types
        print(f"SQL ERROR: {exc}", file=sys.stderr)
        return 1

    df = rel.fetchdf()
    total = len(df)
    truncated = total > args.limit
    if truncated:
        df = df.head(args.limit)

    if args.csv:
        print(df.to_csv(index=False))
    else:
        print(df.to_markdown(index=False))

    print(f"\n({total} rows" + (f", showing first {args.limit})" if truncated else ")"))

    if args.describe and args.data:
        cnt = con.sql(f"SELECT COUNT(*) AS c FROM {args.table}").fetchone()[0]
        print(f"\n# Row count: {cnt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
