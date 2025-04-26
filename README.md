### 📄 `mean_var_std.py`

```python
import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(input_list).reshape(3, 3)

    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().item()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }

    return calculations
```

---

### ▶️ `main.py`

```python
from mean_var_std import calculate

if __name__ == '__main__':
    test_input = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    result = calculate(test_input)
    print(result)
```

---

### ✅ `test_module.py`

```python
import unittest
from mean_var_std import calculate

class TestMeanVarStd(unittest.TestCase):

    def test_valid_input(self):
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertAlmostEqual(result['mean'][2], 4.0)
        self.assertAlmostEqual(result['variance'][2], 6.666666666666667)
        self.assertAlmostEqual(result['standard deviation'][2], 2.581988897471611)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])

if __name__ == '__main__':
    unittest.main()
```

---

### 📝 `README.md`

```markdown
# Mean-Variance-Standard Deviation Calculator

This project calculates statistical values (mean, variance, standard deviation, max, min, sum) from a 3x3 matrix created from a list of 9 numbers using NumPy.

## Features

- **Input**: List of 9 numbers
- **Output**: Dictionary with:
  - Mean
  - Variance
  - Standard deviation
  - Max
  - Min
  - Sum

Each calculated for:
- Axis 0 (columns)
- Axis 1 (rows)
- Flattened array

## Example

```python
>>> from mean_var_std import calculate
>>> calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
  'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.581...],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## Files

- `mean_var_std.py`: Main logic
- `main.py`: Test runner
- `test_module.py`: Unit tests
- `README.md`: Documentation

## Usage

```bash
$ python3 main.py
```

Run tests:

```bash
$ python3 -m unittest test_module.py
```

## Installation

```bash
$ pip install numpy
```

## Error Handling

If input list has less than 9 numbers:

```python
>>> calculate([1, 2, 3])
Raises: ValueError: "List must contain nine numbers."
```

## License

This project is part of the freeCodeCamp Data Analysis with Python curriculum.
```

---

Let me know if you want it zipped, turned into a GitHub repo, or refactored into a class-based structure.
