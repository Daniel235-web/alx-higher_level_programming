#!/usr/bin/python3
"""
   function that finds a peak in a list of unsorted integers
"""
def find_peak(arr):
    """
    Finds a peak in a list of unsorted integers using the divide and conquer strategy.
    Returns the peak element and its index.
    """
    n = len(arr)
    if n == 0:
        return None
    elif n == 1:
        return arr[0]
    elif n == 2:
        return max(arr)
    else:
        mid = n // 2
        if arr[mid] <= arr[mid-1]:
            return find_peak(arr[:mid])
        elif arr[mid] < arr[mid+1]:
            return find_peak(arr[mid+1:])
        else:
            return arr[mid]
