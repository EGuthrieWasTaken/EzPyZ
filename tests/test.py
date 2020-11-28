"""
test.py
~~~~~~~
Runs tests to ensure that EzPyZ is running correctly.
"""

# Standard library.
from typing import Any
# Internal classes/functions
import EzPyZ as ez
from EzPyZ.tools import read_csv, read_excel

def do_test(
        title: str,
        expected: Any,
        got: Any
) -> None:
    """
    Compares the values ``expected`` and ``got``. If they are not equal, a ``ValueError`` is raised.
    Otherwise nothing is returned.
    """
    if expected != got:
        raise ValueError(
                "expected " + title + " to return " + str(expected), ", got " + str(got)
        )

def main() -> None:
    # Testing to see if read functions work.
    csv_data = read_csv("tests/test.csv")
    xl_data = read_excel("tests/test.xlsx")
    do_test("read functions", str(csv_data), str(xl_data))

    # Creating dataframe with csv_data
    df = ez.DataFrame(data=csv_data)

    # Testing to see if mean, median, mode functions work.
    do_test("mean", 166.17, round(df.height_cm.mean(), 2))
    do_test("median", 168, df.height_cm.median())
    do_test("mode", 168, df.height_cm.mode())

    # Testing if standard deviation and variance functions work.
    do_test("standard deviation", 26.17, round(df.weight_kg.stdev(), 2))
    do_test("variance", 685.12, round(df.weight_kg.variance(), 2))

main()