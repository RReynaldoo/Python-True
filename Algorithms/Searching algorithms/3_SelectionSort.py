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