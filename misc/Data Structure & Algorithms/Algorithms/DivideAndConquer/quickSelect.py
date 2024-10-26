# def quickSelect(arr, left, right, k):
#     if left == right:
#         return arr[left]
#     pivot = partition(arr, left, right)
#     if k == pivot:
#         return arr[k]
#     elif k < pivot:
#         return quickSelect(arr, left, pivot-1, k)
#     else:
#         return quickSelect(arr, pivot+1, right, k)


def quickSelect(arr, left, right, k):
    s = partition(arr, left, right)  # Partition the array and get the pivot index
    if s == k - 1:  # Check if the pivot index is the one we're looking for
        return arr[s]  # Return the pivot element as it is the k-th smallest element
    elif k - 1 < s:  # If k-th element is in the left subarray
        return quickSelect(arr, left, s - 1, k)  # Recursively search the left subarray
    else:  # If k-th element is in the right subarray
        return quickSelect(
            arr, s + 1, right, k
        )  # Recursively search the right subarray


def partition(arr, left, right):
    p = arr[left]
    s = left
    for i in range(left + 1, right + 1):
        if arr[i] < p:
            s += 1
            swap(arr, i, s)
    swap(arr, left, s)
    return s


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


arr = [4, 1, 10, 8, 7, 12, 9, 2, 15]
l = 0
r = len(arr) - 1
k = 4
print(quickSelect(arr, l, r, k))
