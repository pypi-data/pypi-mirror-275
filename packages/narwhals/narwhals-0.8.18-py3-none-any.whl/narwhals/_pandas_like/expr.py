from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any
from typing import Callable

from narwhals._pandas_like.series import PandasSeries
from narwhals._pandas_like.utils import register_expression_call
from narwhals._pandas_like.utils import register_namespace_expression_call

if TYPE_CHECKING:
    from typing_extensions import Self

    from narwhals._pandas_like.dataframe import PandasDataFrame


class PandasExpr:
    def __init__(  # noqa: PLR0913
        self,
        call: Callable[[PandasDataFrame], list[PandasSeries]],
        *,
        depth: int,
        function_name: str,
        root_names: list[str] | None,
        output_names: list[str] | None,
        implementation: str,
    ) -> None:
        self._call = call
        self._depth = depth
        self._function_name = function_name
        self._root_names = root_names
        self._depth = depth
        self._output_names = output_names
        self._implementation = implementation

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"PandasExpr("
            f"depth={self._depth}, "
            f"function_name={self._function_name}, "
            f"root_names={self._root_names}, "
            f"output_names={self._output_names}"
        )

    @classmethod
    def from_column_names(
        cls: type[Self], *column_names: str, implementation: str
    ) -> Self:
        return cls(
            lambda df: [
                PandasSeries(
                    df._dataframe.loc[:, column_name],
                    implementation=df._implementation,
                )
                for column_name in column_names
            ],
            depth=0,
            function_name="col",
            root_names=list(column_names),
            output_names=list(column_names),
            implementation=implementation,
        )

    def cast(
        self,
        dtype: Any,
    ) -> Self:
        return register_expression_call(self, "cast", dtype)

    def __eq__(self, other: PandasExpr | Any) -> Self:  # type: ignore[override]
        return register_expression_call(self, "__eq__", other)

    def __ne__(self, other: PandasExpr | Any) -> Self:  # type: ignore[override]
        return register_expression_call(self, "__ne__", other)

    def __ge__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__ge__", other)

    def __gt__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__gt__", other)

    def __le__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__le__", other)

    def __lt__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__lt__", other)

    def __and__(self, other: PandasExpr | bool | Any) -> Self:
        return register_expression_call(self, "__and__", other)

    def __rand__(self, other: Any) -> Self:
        return register_expression_call(self, "__rand__", other)

    def __or__(self, other: PandasExpr | bool | Any) -> Self:
        return register_expression_call(self, "__or__", other)

    def __ror__(self, other: Any) -> Self:
        return register_expression_call(self, "__ror__", other)

    def __add__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__add__", other)

    def __radd__(self, other: Any) -> Self:
        return register_expression_call(self, "__radd__", other)

    def __sub__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__sub__", other)

    def __rsub__(self, other: Any) -> Self:
        return register_expression_call(self, "__rsub__", other)

    def __mul__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__mul__", other)

    def __rmul__(self, other: Any) -> Self:
        return register_expression_call(self, "__rmul__", other)

    def __truediv__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__truediv__", other)

    def __rtruediv__(self, other: Any) -> Self:
        return register_expression_call(self, "__rtruediv__", other)

    def __floordiv__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__floordiv__", other)

    def __rfloordiv__(self, other: Any) -> Self:
        return register_expression_call(self, "__rfloordiv__", other)

    def __pow__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__pow__", other)

    def __rpow__(self, other: Any) -> Self:
        return register_expression_call(self, "__rpow__", other)

    def __mod__(self, other: PandasExpr | Any) -> Self:
        return register_expression_call(self, "__mod__", other)

    def __rmod__(self, other: Any) -> Self:
        return register_expression_call(self, "__rmod__", other)

    # Unary

    def __invert__(self) -> Self:
        return register_expression_call(self, "__invert__")

    # Reductions

    def sum(self) -> Self:
        return register_expression_call(self, "sum")

    def mean(self) -> Self:
        return register_expression_call(self, "mean")

    def std(self, *, ddof: int = 1) -> Self:
        return register_expression_call(self, "std", ddof=ddof)

    def any(self) -> Self:
        return register_expression_call(self, "any")

    def all(self) -> Self:
        return register_expression_call(self, "all")

    def max(self) -> Self:
        return register_expression_call(self, "max")

    def min(self) -> Self:
        return register_expression_call(self, "min")

    # Other
    def is_between(
        self, lower_bound: Any, upper_bound: Any, closed: str = "both"
    ) -> Self:
        return register_expression_call(
            self, "is_between", lower_bound, upper_bound, closed
        )

    def is_null(self) -> Self:
        return register_expression_call(self, "is_null")

    def fill_null(self, value: Any) -> Self:
        return register_expression_call(self, "fill_null", value)

    def is_in(self, other: Any) -> Self:
        return register_expression_call(self, "is_in", other)

    def filter(self, *predicates: Any) -> Self:
        from narwhals._pandas_like.namespace import PandasNamespace

        plx = PandasNamespace(self._implementation)
        expr = plx.all_horizontal(*predicates)
        return register_expression_call(self, "filter", expr)

    def drop_nulls(self) -> Self:
        return register_expression_call(self, "drop_nulls")

    def sort(self, *, descending: bool = False) -> Self:
        return register_expression_call(self, "sort", descending=descending)

    def n_unique(self) -> Self:
        return register_expression_call(self, "n_unique")

    def cum_sum(self) -> Self:
        return register_expression_call(self, "cum_sum")

    def unique(self) -> Self:
        return register_expression_call(self, "unique")

    def diff(self) -> Self:
        return register_expression_call(self, "diff")

    def shift(self, n: int) -> Self:
        return register_expression_call(self, "shift", n)

    def sample(
        self,
        n: int | None = None,
        fraction: float | None = None,
        *,
        with_replacement: bool = False,
    ) -> Self:
        return register_expression_call(
            self, "sample", n, fraction=fraction, with_replacement=with_replacement
        )

    def alias(self, name: str) -> Self:
        # Define this one manually, so that we can
        # override `output_names` and not increase depth
        return self.__class__(
            lambda df: [series.alias(name) for series in self._call(df)],
            depth=self._depth,
            function_name=self._function_name,
            root_names=self._root_names,
            output_names=[name],
            implementation=self._implementation,
        )

    def over(self, keys: list[str]) -> Self:
        def func(df: PandasDataFrame) -> list[PandasSeries]:
            if self._output_names is None:
                msg = (
                    "Anonymous expressions are not supported in over.\n"
                    "Instead of `nw.all()`, try using a named expression, such as "
                    "`nw.col('a', 'b')`\n"
                )
                raise ValueError(msg)
            tmp = df.group_by(keys).agg(self)
            tmp = df.select(keys).join(tmp, how="left", left_on=keys, right_on=keys)
            return [tmp[name] for name in self._output_names]

        return self.__class__(
            func,
            depth=self._depth + 1,
            function_name=self._function_name + "->over",
            root_names=self._root_names,
            output_names=self._output_names,
            implementation=self._implementation,
        )

    def is_duplicated(self) -> Self:
        return register_expression_call(self, "is_duplicated")

    def is_unique(self) -> Self:
        return register_expression_call(self, "is_unique")

    def null_count(self) -> Self:
        return register_expression_call(self, "null_count")

    def is_first_distinct(self) -> Self:
        return register_expression_call(self, "is_first_distinct")

    def is_last_distinct(self) -> Self:
        return register_expression_call(self, "is_last_distinct")

    @property
    def str(self) -> PandasExprStringNamespace:
        return PandasExprStringNamespace(self)

    @property
    def dt(self) -> PandasExprDateTimeNamespace:
        return PandasExprDateTimeNamespace(self)


class PandasExprStringNamespace:
    def __init__(self, expr: PandasExpr) -> None:
        self._expr = expr

    def ends_with(self, suffix: str) -> PandasExpr:
        return register_namespace_expression_call(
            self._expr,
            "str",
            "ends_with",
            suffix,
        )

    def head(self, n: int = 5) -> PandasExpr:
        return register_namespace_expression_call(
            self._expr,
            "str",
            "head",
            n,
        )

    def to_datetime(self, format: str | None = None) -> PandasExpr:  # noqa: A002
        return register_namespace_expression_call(
            self._expr,
            "str",
            "to_datetime",
            format,
        )


class PandasExprDateTimeNamespace:
    def __init__(self, expr: PandasExpr) -> None:
        self._expr = expr

    def year(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "year")

    def month(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "month")

    def day(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "day")

    def hour(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "hour")

    def minute(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "minute")

    def second(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "second")

    def millisecond(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "millisecond")

    def microsecond(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "microsecond")

    def ordinal_day(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "ordinal_day")

    def total_minutes(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "total_minutes")

    def total_seconds(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "total_seconds")

    def total_milliseconds(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "total_milliseconds")

    def total_microseconds(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "total_microseconds")

    def total_nanoseconds(self) -> PandasExpr:
        return register_namespace_expression_call(self._expr, "dt", "total_nanoseconds")
