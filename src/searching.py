"""
Module: searching.py
Description: This module contains an implementation of binary search algorithm.
"""


def binary_search(arr, target):
    """
    Search for a target value in sorted list using the binary search algorithm.

    Parameters:
    arr (list): A list of sorted elements.
    target (any): The element to search for.

    Returns:
    int: The index of the target element if found; otherwise, -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Target is not found in the list.
    return -1


if __name__ == "__main__":
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 4
    print(f"Index of {target}:", binary_search(sorted_list, target))
