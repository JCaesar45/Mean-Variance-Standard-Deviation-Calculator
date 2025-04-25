# Mean-Variance-Standard Deviation Calculator

This project calculates statistical values (mean, variance, standard deviation, max, min, sum)
from a 3x3 matrix created from a list of 9 numbers using NumPy.

---

## Features

- Input: List of 9 numbers
- Output: Dictionary with calculations for:
  - Mean
  - Variance
  - Standard deviation
  - Max
  - Min
  - Sum

Each value is calculated across:
  - Axis 0 (columns)
  - Axis 1 (rows)
  - Flattened array

---

## Example

Function call:
>>> calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

Expected output:
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
  'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.581...],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}

---

## Files

mean_var_std.py   -> Main logic function
main.py           -> Test runner script
test_module.py    -> Unit tests
README.md         -> Project description

---

## Usage

$ python3 main.py

Run tests:

$ python3 -m unittest test_module.py

---

## Installation

$ pip install numpy

---

## Error Handling

If input list has less than 9 numbers:

>>> calculate([1, 2, 3])
Raises: ValueError: "List must contain nine numbers."

---

## License

This project is part of the freeCodeCamp Data Analysis with Python curriculum.
