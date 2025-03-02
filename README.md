# Algorithms and Data Structures Portfolio

This project is a showcase of basic algorithms and data structures implemented in Python. It includes implementations for sorting, searching algorithms, and common data structures, along with unit tests and documentation on how to run the code.

## Purpose

- Demonstrate understanding of common algorithms (e.g., sorting, binary search) and data structures (e.g., linked list, stack, queue).
- Provide clear documentation and tests to support code quality.

## Project Structure

```bash
algorithms-ds/
├── README.md
├── src/
│   └── sorting.py
└── tests/
    └── test_sorting.py
```

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/denn4617/algorithms-ds.git
   cd algorithms-ds
   ```

2. **Run the code:**

You can import the functions and classes from the modules in your Python scripts.

Example:

```python
from src.sorting import merge_sort, quick_sort
from src.searching import binary_search

# Sorting example:
unsorted_list = [5, 3, 8, 4, 2]
print("Merge Sort:", merge_sort(unsorted_list))
print("Quick Sort:", quick_sort(unsorted_list))

# Binary Search example:
sorted_list = [1, 2, 3, 4, 5]
print("Index of 3:", binary_search(sorted_list, 3))
```

3. **Run the tests:**

Use Python’s unittest framework:

```bash
python -m unittest discover tests
```
