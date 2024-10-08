def binarySearch(target, sortedLyst):
    left = 0                                # Initialize the left boundary to 0, first index of the list
    right = len(sortedLyst) - 1             # Initialize the right boundary to the last index of the list
    while left <= right:                    # Continue searching while the left boundary is less than or equal to the right boundary
        midpoint = (left + right) // 2      # Calculate the midpoint of the current search range
        if target == sortedLyst[midpoint]:  # Check if the target is found at the midpoint
            return midpoint                 # Return the index of the target
        elif target < sortedLyst[midpoint]: # Check if the target is less than the midpoint
            right = midpoint - 1            # Update the right boundary to midpoint - 1
        else:                               # Target is greater than the midpoint
            left = midpoint + 1             # Update the left boundary to midpoint + 1
    return -1                               # Return -1 if the target is not found