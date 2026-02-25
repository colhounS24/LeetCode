"""
Place to practice my sorting algos
"""

def bubble_sort(arr):
        """
        - This works by continuosly swapping the entries, effectively pushing the largest to the end
        - very slow
        - O(n^2)
        """
        swapped = True
        while swapped:
            swapped= False
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True
        return arr

def selection_sort(arr):
    """
    Works by comparing each element against the rest and then subbing it in.
    O(n^2)

    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

def insertion_sort(arr):
    # assume that index 0 is correct
    for i in range(1,len(arr)):
        # current is the variable that we are currently comparing
        # j is the previous check to see where it fits in and will be used the "push" the array
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >current:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = current
    return arr     

def merge_sort(arr):
    length: int = len(arr)

    if length <=1:
        return
    
    middle: int = int(length / 2)

    left_array = []
    right_array = []

    for i in range(length):
        if i < middle:
            left_array.append(arr[i])
        else:
            right_array.append(arr[i])
    
    # recursivly call until we have lengths of 1 ,working down the lhs first
    merge_sort(left_array)
    merge_sort(right_array)
    _merge(left_array, right_array, arr)

    return arr
        
# Helper for merge_sort
def _merge(left_array, right_array, array):
    
    left_size = int(len(array) /2)
    right_size = int(len(array) - left_size)

    i = 0
    l = 0
    r = 0
    # indices

    # check conditions for merging

    while l < left_size and r < right_size:
        if left_array[l] < right_array[r]:
            array[i] = left_array[l]
            i+=1
            l+=1
        else:
            array[i] = right_array[r]
            i+=1
            r+=1

    while l < left_size:
        array[i] = left_array[l]
        i+= 1
        l+=1

    while r < right_size:
        array[i] = right_array[r]
        i+=1
        r+=1

def quick_sort(arr: list[int], start: int, end: int):
    # Base case
    if end <= start:
        return 
    
    
    
    pivot= _partition(arr, start, end)
    quick_sort(arr, start, pivot -1)
    quick_sort(arr, pivot+1, end)

def _partition(arr: list[int],start: int, end: int) -> int:
    # returns the location of the pivot
    pivot = arr[end]
    i = start - 1
    j = start

    for j in range(start,end):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j], arr[i]

    i+=1
    arr[i], arr[end] = arr[end], arr[i]
    return i

