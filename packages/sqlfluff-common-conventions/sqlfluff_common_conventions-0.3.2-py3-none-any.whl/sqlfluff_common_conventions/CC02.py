"""Implementation of Rule CC02."""

from sqlfluff.core.rules import BaseRule, LintResult, RuleContext
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


class Rule_CC02(BaseRule):
    """Do not have a datetime, time, or timestamp column that does not end with `at`.

    **Anti-pattern**

    .. code-block:: sql

        create or replace table tbl (
            created datetime,
            updated time,
            deleted timestamp
        )

    **Best practice**

    End datetime, time, and timestamp columns with `at`.

    .. code-block:: sql

        create or replace table tbl (
            created_at datetime,
            updated_at time,
            deleted_at timestamp
        )
    """

    groups = ("all", "convention")

    crawl_behaviour = SegmentSeekerCrawler(
        {
            "column_definition",
            "select_clause_element",
        }
    )
    config_keywords = ["naming_case"]
    is_fix_compatible = False

    def _eval(self, context: RuleContext):
        """Find rule violations and provide fixes."""

        self.naming_case: str

        segment = context.segment

        if segment.is_type("select_clause_element"):
            function = segment.get_child("function")
            if not function:
                return None

            function_name = function.get_child("function_name")
            alias_expression = segment.get_child("alias_expression")

            if not (function_name.raw_upper == "CAST" and alias_expression):
                return None

            identifier = alias_expression.get_child("identifier").raw
            datatype = function.get_child("bracketed").get_child("data_type").raw
        else:  # column_definition
            assert segment.is_type("column_definition")
            identifier = segment.get_child("identifier").raw
            datatype = segment.get_child("data_type")

            if not datatype:  # account for views, which are parsed like tables
                return None

            datatype = datatype.raw

        if datatype.upper() in ["DATETIME", "TIME", "TIMESTAMP"]:
            if self.naming_case == "snake" and not (identifier.endswith("_at")):
                return LintResult(
                    anchor=context.segment,
                    description="Datetime, time, or timestamp column does not end with `_at`.",
                )

            if self.naming_case in ["dromedary", "pascal"] and (
                not (identifier.endswith("At"))
            ):
                return LintResult(
                    anchor=context.segment,
                    description="Datetime, time, or timestamp column does not end with `At`.",
                )
