"""
Module: sorting.py
Description: This module contains implementations of common sorting algorithms:
             - Merge Sort
             - Quick sort.
"""


def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A new sorted list.
    """
    # Base case
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves.
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves.
    return _merge(left_half, right_half)


def _merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    Parameters:
    left (list): First sorted list.
    right (list): Second sorted list.

    Returns:
    list: A merged and sorted list.
    """
    merged = []
    left_index, right_index = 0, 0

    # Compare elements from both lists and merge them in sorted order.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from left or right list.
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A new sorted list.
    """
    # Base case
    if len(arr) <= 1:
        return arr

    # Setting the pivot as the last element.
    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]

    # Recursively apply quick sort and concatenate the results.
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    # Example usage of the sorting algorithms.
    sample_list = [5, 3, 8, 4, 2, 7, 1, 10]
    print("Original list:", sample_list)
    print("Merge Sort Result:", merge_sort(sample_list))
    print("Quick Sort Result:", quick_sort(sample_list))
