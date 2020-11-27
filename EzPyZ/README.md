## Table of Contents

[column.py](#columnpy)

[dataframe.py](#dataframepy)

# [column.py](column.py)

## Cheatsheet

|                             Function Header                             |                      Quick Description                      |
|:-----------------------------------------------------------------------:|:-----------------------------------------------------------:|
| [``__init__(title, values)``](#__init__title-str-values-listany---none) |             Initializes the ``Column`` object.              |
|                    [``__repr__()``](#__repr__---str)                    |     Returns basic ``Column`` information for debugging.     |
|                     [``__str__()``](#__str__---str)                     |         Returns a string of the ``Column`` object.          |
|                [``get_values()``](#get_values---listany)                |         Returns the ``values`` attribute as a list.         |
|                      [``length()``](#length---int)                      |       Returns the length of the ``values`` attribute.       |
|                       [``mean()``](#mean---float)                       |        Returns the mean of the ``values`` attribute.        |
|                     [``median()``](#median---float)                     |       Returns the median of the ``values`` attribute.       |
|                       [``mode()``](#mode---float)                       |        Returns the mode of the ``values`` attribute.        |
|                      [``stdev()``](#stdev---float)                      | Returns the standard deviation of the ``values`` attribute. |
|       [``set_values(values)``](#set_valuesvalues-listany---none)        |               Sets the ``values`` attribute.                |
|                       [``title()``](#title---str)                       |              Returns the ``title`` attribute.               |
|                   [``variance()``](#variance---float)                   |      Returns the variance of the ``values`` attribute.      |

## \_\_init__(title: str, values: List[Any]) -> None

|    Name    |    Type   | Required | Default Value |                      Description                      |
|:----------:|:---------:|:--------:|:-------------:|:-----------------------------------------------------:|
|  ``title`` |   String  |    Yes   |      N/A      |      A string containing the title of the column.     |
| ``values`` | List[Any] |    Yes   |      N/A      | A list containing the values in the column, in order. |

Initializes the ``Column`` object. ``Column`` objects are intended to be used internally within ``DataFrame`` objects, but their functions may also be of use to end users.  
Example:

```python
import EzPyZ as ez

# Initialize a column object.
col = ez.Column("weight_kg", [32.2, 64.3, 59.9, 95.4, 104.2, 63.1])
```

## \_\_repr__() -> str

Returns basic ``Column`` information for debugging.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("weight_kg", [32.2, 64.3, 59.9, 95.4, 104.2, 63.1])

# Get object info for col.
print(repr(col))
```

Which would print:

```text
Column(title=weight_kg, values=[32.2, 64.3, 59.9, 95.4, 104.2, 63.1])
```

## \_\_str__() -> str

Prints the ``Column`` for viewing.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("weight_kg", [32.2, 64.3, 59.9, 95.4, 104.2, 63.1])

# Print the column.
print(col)
```

Which would print:

```text
weight_kg
32.2
64.3
59.9
95.4
104.2
63.1
```

## get_values() -> List[Any]

Returns the ``Column.values`` attribute.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("weight_kg", [32.2, 64.3, 59.9, 95.4, 104.2, 63.1])

# Print the column values.
print(col.get_values())
```

Which would print:

```text
[32.2, 64.3, 59.9, 95.4, 104.2, 63.1]
```

## length() -> int

Returns the length of the ``Column.values`` attribute.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("weight_kg", [32.2, 64.3, 59.9, 95.4, 104.2, 63.1])

# Print the length of the column.
print(col.length())
```

Which would print:

```text
6
```

## mean() -> float

Returns the mean of the ``Column.values`` attribute.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("weight_kg", [32.2, 64.3, 59.9, 95.4, 104.2, 63.1])

# Print the mean of the column.
print(col.mean())
```

Which would print:

```text
69.85
```

## median() -> float

Returns the median of the ``Column.values`` attribute.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("weight_kg", [32.2, 64.3, 59.9, 95.4, 104.2, 63.1])

# Print the median of the column.
print(col.median())
```

Which would print:

```text
63.7
```

## mode() -> float

Returns the median of the ``Column.values`` attribute.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("height_cm", [134, 168, 149, 201, 177, 168])

# Print the mode of the column.
print(col.mode())
```

Which would print:

```text
168
```

## stdev() -> float

Returns the standard deviation of the ``Column.values`` attribute.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("height_cm", [134, 168, 149, 201, 177, 168])

# Print the standard deviation of the column.
print(col.stdev())
```

Which would print:

```text
23.094732444145496
```

## set_values(values: List[Any]) -> None

|    Name    |    Type   | Required | Default Value |                      Description                      |
|:----------:|:---------:|:--------:|:-------------:|:-----------------------------------------------------:|
| ``values`` | List[Any] |    Yes   |      N/A      | A list containing the values in the column, in order. |

Sets the ``Column.values`` attribute.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("height_cm", [134, 168, 149, 201, 177, 168])

# Set new Column values.
col.set_values([134, 168, 149, 201, 177, 168, 190])
```

## title() -> str

Returns the ``Column.title`` attribute.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("height_cm", [134, 168, 149, 201, 177, 168])

# Print the variance of the column.
print(col.title())
```

Which would print:

```text
height_cm
```

## variance() -> float

Returns the standard deviation of the ``Column.values`` attribute.  
Example:

```python
from EzPyZ.column import Column

# Initialize a column object.
col = Column("height_cm", [134, 168, 149, 201, 177, 168])

# Print the variance of the column.
print(col.variance())
```

Which would print:

```text
533.3666666666667
```

# [dataframe.py](dataframe.py)

## Cheatsheet

## \_\_init__(data: Union[pd.DataFrame, Dict[str, List[Any]]], columns=None) -> None

## \_\_repr__() -> str
