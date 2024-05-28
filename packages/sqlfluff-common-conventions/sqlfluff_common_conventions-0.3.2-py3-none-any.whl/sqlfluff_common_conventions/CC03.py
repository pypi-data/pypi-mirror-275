"""Implementation of Rule CC03."""

from sqlfluff.core.rules import BaseRule, LintResult, RuleContext
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


class Rule_CC03(BaseRule):
    """Do not have a date column that does not end with `date`.

    **Anti-pattern**

    .. code-block:: sql

        create or replace table tbl (
            created date
        )

    **Best practice**

    End date columns with `date`.

    .. code-block:: sql

        create or replace table tbl (
            created_date date
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

        if datatype.upper() == "DATE":
            if self.naming_case == "snake" and not (identifier.endswith("_date")):
                return LintResult(
                    anchor=context.segment,
                    description="Date column does not end with `_date`.",
                )

            if self.naming_case in ["dromedary", "pascal"] and (
                not (identifier.endswith("Date"))
            ):
                return LintResult(
                    anchor=context.segment,
                    description="Date column does not end with `Date`.",
                )
