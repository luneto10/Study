from binarySearch import binary_search


def matrix_search(matrix, key):
    if not matrix or not matrix[0]:
        return (-1, -1)
    
    m = len(matrix)
    n = len(matrix[0])
    
    i = 0       
    j = n - 1 
    
    while i < m and j >= 0:
        if matrix[i][j] == key:
            return (i, j)
        elif matrix[i][j] > key:
            j -= 1
        else:
            i += 1
    return (-1, -1)



matrix = [
    [1,2,4,5,10],
    [11,14,20,43,44],
    [50,51,60,90,94]
]
key = 44
print(matrix_search(matrix, key))
