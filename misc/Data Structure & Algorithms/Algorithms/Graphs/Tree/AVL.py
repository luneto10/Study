def preSorting(arr: list):
    arr.sort()
    
    min_diff = float("inf")
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < min_diff:
            min_diff = abs(arr[i] - arr[i + 1])
    return min_diff

arr = [11,5,4,7,20]
print(preSorting(arr))
        