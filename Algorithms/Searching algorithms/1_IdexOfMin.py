def indexOfMin(lyst):
    minIndex = 0                                            # Initialize the minimum index to 0, assuming the first element is the smallest
    currentIndex = 1                                        # Initialize the current index to 1, starting from the second element
    while currentIndex < len(lyst):                         # Loop through the list until we reach the end
        if lyst[currentIndex] < lyst[minIndex]:             # Check if the current element is smaller than the minimum element found so far
            minIndex = currentIndex                         # Update the minimum index to the current index
        currentIndex += 1                                   # Move to the next element in the list
    return minIndex                                         # Return the index of the minimum value