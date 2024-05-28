# sqlfluff-common-conventions

A plugin for rules that enforce common SQL conventions not available in SQLFluff, compatible with BigQuery SQL and Databricks SQL.

## Rules

As of 8 May 2024, all rules are compatible with snake, dromedary, and pascal case.

- CC01: Start boolean columns with `is` or `has`.
- CC02: End datetime, time, and timestamp columns with `at`.
- CC03: End date columns with `date`.
- CC04: Only allow a list of configurable strings to be used in identifiers.
- CC05: Block a list of configurable strings from being used in identifiers.
- CC06: Ensure column and table names match a given regex.