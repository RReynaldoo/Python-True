def binary_search(arr, target):
    """
    Searches for the target element in the given array using binary search.

    Args:
        arr (list): The sorted array to search in.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # not found