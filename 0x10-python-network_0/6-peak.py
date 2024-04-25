#!/usr/bin/python3
def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if not list_of_integers:  # Empty list check
        return None

    # Binary search approach
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        # If the element to the right of mid is greater, peak must be on the right
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        # Otherwise, peak must be on the left
        else:
            right = mid

    return list_of_integers[left]
