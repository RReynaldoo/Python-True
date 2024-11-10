def insertionSort(lyst):
    i = 1                               # Start from the second element (index 1)
    while i < len(lyst):                        # Iterate through the list
        itemToInsert = lyst[i]          # Consider the current element as the item to be inserted
        j = i - 1                       # Initialize the index for the inner loop

        while j >= 0:                   # Shift elements to the right until the correct position for the itemToInsert is found
            if itemToInsert < lyst[j]:                     # If the itemToInsert is smaller than the current element, shift the current element to the right
                lyst[j + 1] = lyst[j]
                j -= 1
            else:                       # If the itemToInsert is not smaller, the correct position is found, so break the loop
                break

        lyst[j + 1] = itemToInsert      # Insert the itemToInsert at the correct position
        i += 1                          # Move to the next element in the list