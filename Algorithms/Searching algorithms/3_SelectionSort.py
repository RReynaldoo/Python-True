def selectionSort(lyst):
    i = 0                                   # Initialize the index to 0
    while i < len(lyst) -1:                 # Loop through the list until the second last element
        min_index = i                       # Initialize the minimum index to the current index
        j = i + 1                           # Initialize the inner loop index to the next element
        while j < len(lyst):                 # Loop through the remaining elements
            if lyst[j] < lyst[min_index]:   # Check if the current element is smaller than the minimum element
                min_index = j               # Update the minimum index
            j +=1                           # Move to the next element
        if min_index !=i:                   # Check if the minimum index is not the current index
            swap(lyst,min_index,i)          # Swap the elements
        i +=1                               # Move to the next element
#---------------------------------------------------

def swap(lyst, a, b):
    temp = lyst[a]
    lyst[a] = lyst[b]
    lyst[b] = temp
#---------------------------------------------------

lyst = [5,3,1,2,4]
print(lyst)
selectionSort(lyst)
print(lyst)
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