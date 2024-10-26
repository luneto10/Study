import random

def mergeSort(array):
    n = len(array)
    if n > 1:
        left = array[:n//2]
        right = array[n//2:]
        
        mergeSort(left)
        mergeSort(right)
        merge(left, right, array)
        return array
        
def merge(arrayA: list, arrayB: list, array: list):
    i = j = k = 0
    while i < len(arrayA) and j < len(arrayB):
        if arrayA[i] <= arrayB[j]:
            array[k] = arrayA[i]
            i += 1
        else:
            array[k] = arrayB[j]
            j += 1
        k += 1

    while i < len(arrayA):
        array[k] = arrayA[i]
        i += 1
        k += 1

    while j < len(arrayB):
        array[k] = arrayB[j]
        j += 1
        k += 1
    return array

random_numbers = [random.randint(-10, 1000) for _ in range(80)]
print(mergeSort(random_numbers))