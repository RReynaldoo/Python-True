def bubbleSort(lyst):
    n = len(lyst)                           # Get the length of the list
    while n > 1:                            # Continue sorting until the list is sorted
        i = 1                               # Initialize the index to 1, starting from the second element
        while i < n:                        # Loop through the list until the end
            if lyst[i] < lyst[i-1]:         # Check if the current element is smaller than the previous element
                swap(lyst,i,i-1)            # Swap the elements
            i += 1                          # Move to the next element
        n -= 1                              # Decrement the length of the list, as the largest element is bubbled to the end
#---------------------------------------------------

def swap(lyst, a, b):
    temp = lyst[a]
    lyst[a] = lyst[b]
    lyst[b] = temp

#---------------------------------------------------(Tweaked version that corresponds to my notes)
def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        swapped = False         # Flag to check if any swaps were made
        i = 1
        while i < n:
            if lyst[i] < lyst[i-1]:
                lyst[i], lyst[i-1] = lyst[i-1], lyst[i]  # Swap elements
                swapped = True  # Set flag to True if a swap was made
            i += 1
        if not swapped:         # If no swaps were made, the list is already sorted
            break
        n -= 1
    return lyst