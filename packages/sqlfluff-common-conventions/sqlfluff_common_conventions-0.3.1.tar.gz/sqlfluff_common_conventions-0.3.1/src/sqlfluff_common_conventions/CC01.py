"""Implementation of Rule CC01."""

from sqlfluff.core.rules import BaseRule, LintResult, RuleContext
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


class Rule_CC01(BaseRule):
    """Do not have a boolean column that does not start with `is` or `has`.

    **Anti-pattern**

    .. code-block:: sql

        create or replace table tbl (
            happy bool,
            money bool,
            created_at datetime,
            updated_at datetime
        )

    **Best practice**

    Start boolean columns with `is` or `has`.

    .. code-block:: sql

        create or replace table tbl (
            is_happy bool,
            has_money bool,
            created_at datetime,
            updated_at datetime
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

        if datatype.upper() in ["BOOL", "BOOLEAN"]:
            if self.naming_case == "snake" and not (
                identifier.startswith("is_") or identifier.startswith("has_")
            ):
                return LintResult(
                    anchor=context.segment,
                    description="Boolean column does not start with `is_` or `has_`.",
                )

            if self.naming_case == "dromedary" and (
                not (identifier.startswith("is") or identifier.startswith("has"))
                or (
                    identifier.startswith("is")
                    and len(identifier) > 2
                    and not identifier[2].isupper()
                    and not identifier[2].isdigit()
                )
                or (
                    identifier.startswith("has")
                    and len(identifier) > 3
                    and not identifier[3].isupper()
                    and not identifier[3].isdigit()
                )
            ):
                return LintResult(
                    anchor=context.segment,
                    description="Boolean column does not start with `is` or `has`.",
                )

            if self.naming_case == "pascal" and (
                not (identifier.startswith("Is") or identifier.startswith("Has"))
                or (
                    identifier.startswith("Is")  # prevent e.g. Isotopic from passing
                    and len(identifier) > 2
                    and not identifier[2].isupper()
                    and not identifier[2].isdigit()
                )
                or (
                    identifier.startswith("Has")  # prevent e.g. Hashbrowns from passing
                    and len(identifier) > 3
                    and not identifier[3].isupper()
                    and not identifier[3].isdigit()
                )
            ):
                return LintResult(
                    anchor=context.segment,
                    description="Boolean column does not start with `Is` or `Has`.",
                )
