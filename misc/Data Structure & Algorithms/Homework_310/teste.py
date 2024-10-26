def findSmallest(arr):
    if not arr:
        return None
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest


def findSmallestRecursive(arr, low, high):
    if low == high:
        return arr[low]

    mid_index = (low + high) // 2

    left_smallest = findSmallestRecursive(arr, low, mid_index)
    right_smallest = findSmallestRecursive(arr, mid_index + 1, high)

    if left_smallest < right_smallest:
        return left_smallest

    return right_smallest


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    return arr


arr = [5, 3, 6, 2, 10, 5, 30,20, 5,2, 31,20,5,10]

def findDuplicateElementCount(arr, low, high, s):
    if low == high:
        if arr[low] == s:
            return 1
        else:
            return 0
    mid = (low + high) // 2
    left = findDuplicateElementCount(arr, low, mid, s)
    right = findDuplicateElementCount(arr, mid + 1, high, s)
    return left + right

# print(findSmallest(arr))
# print(findSmallestRecursive(arr, 0, len(arr) - 1))
print(findDuplicateElementCount(arr, 0, len(arr) - 1, 5))


def bfs_non_recursive(start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    result = [start_node]
    
    while queue:
        current_node = queue.popleft()
        for neighbor in current_node:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result