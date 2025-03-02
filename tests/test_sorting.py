import unittest
from src.sorting import merge_sort, quick_sort


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        # Setup a list of test cases that will be used in each test.
        self.unsorted_list = [34, 7, 23, 32, 5, 62]
        self.sorted_list = sorted(self.unsorted_list)
        self.empty_list = []
        self.single_element = [1]
        self.duplicates_list = [5, 3, 8, 3, 9, 1, 5]

    def test_merge_sort_regular(self):
        # Test merge_sort with a regular unsorted list.
        self.assertEqual(merge_sort(self.unsorted_list), self.sorted_list)

    def test_quick_sort_regular(self):
        # Test quick_sort with a regular unsorted list.
        self.assertEqual(quick_sort(self.unsorted_list), self.sorted_list)

    def test_empty_list(self):
        # Test both functions with an empty list - should return empty list.
        self.assertEqual(merge_sort(self.empty_list), [])
        self.assertEqual(quick_sort(self.empty_list), [])

    def test_single_element(self):
        # A single-element list should remain unchanged after sorting.
        self.assertEqual(merge_sort(self.single_element), self.single_element)
        self.assertEqual(quick_sort(self.single_element), self.single_element)

    def test_duplicates(self):
        # Sorting lists with duplicate elements.
        expected = sorted(self.duplicates_list)
        self.assertEqual(merge_sort(self.duplicates_list), expected)
        self.assertEqual(quick_sort(self.duplicates_list), expected)


if __name__ == "__main__":
    unittest.main()
