"""Run a small dependency-free example of the Python layout conventions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReportQuery:
    """Keep the selected columns and ordering in one immutable value.

    This internal value needs no input validation. A public input DTO would
    follow the host project's validation model instead.
    """

    columns: tuple[str, ...] = ()
    order_by: str | None = None

    def select(
        self,
        *columns: str,
    ) -> ReportQuery:
        return ReportQuery(
            columns=columns,
            order_by=self.order_by,
        )

    def order(
        self,
        *,
        by: str,
    ) -> ReportQuery:
        return ReportQuery(
            columns=self.columns,
            order_by=by,
        )


def main() -> None:
    # A new immutable query preserves the original query's state.
    query = ReportQuery()
    result = (
        query
        .select(
            "name",
            "status",
        )
        .order(by="name")
    )
    assert query.columns == ()
    assert result.columns == ("name", "status")
    assert result.order_by == "name"
    print("Python style example passed.")


if __name__ == "__main__":
    main()
