def ternary_Search(arr, key):
    L = 0
    R = len(arr) - 1
    while L <= R:
        mid1 = L + (R - L) // 3
        mid2 = R - (R - L) // 3
        
        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2
        
        if key < arr[mid1]:
            R = mid1 - 1
        elif key > arr[mid2]:
            L = mid2 + 1
        else:
            L = mid1 + 1
            R = mid2 - 1
    return -1

arr = [1,2,3,4,5,6,7,8,9]

print(ternary_Search(arr, 5))