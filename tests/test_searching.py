import unittest
from src.searching import binary_search


class TestSearchingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test that binary search returns the correct index for an existing element
    def test_existing_element(self):
        self.assertEqual(binary_search(self.sorted_list, 4), 3)

    # Test that binary search returns -1 for a non-existent element.
    def test_nonexistent_element(self):
        self.assertEqual(binary_search(self.sorted_list, 10), -1)

    # Binary search on an empty list should return -1.
    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)


if __name__ == "__main__":
    unittest.main()
