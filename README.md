# Mean-Variance-Standard Deviation Calculator

This project is part of the freeCodeCamp Data Analysis with Python course. It calculates key statistics — mean, variance, standard deviation, max, min, and sum — for a 3x3 matrix formed from a list of 9 numbers.

---

## 📌 Features

- Accepts a list of **exactly 9 numbers**
- Converts list into a **3x3 NumPy array**
- Calculates the following statistics:
  - **Mean**
  - **Variance**
  - **Standard Deviation**
  - **Max**
  - **Min**
  - **Sum**
- Returns values for:
  - Each column (`axis 0`)
  - Each row (`axis 1`)
  - The flattened array

---

## 💡 Example

```python
from mean_var_std import calculate

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
