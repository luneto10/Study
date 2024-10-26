def findBiggestElement(arr, left, right):
    if left == right:
       return arr[left]
   
    mid = (left + right) // 2
    
    max1 = findBiggestElement(arr, left, mid)
    max2 = findBiggestElement(arr, mid+1, right)
    return max(max1, max2)

findBiggestElement([1, 2, 11, 4, 5,-2,4], 0, 6)