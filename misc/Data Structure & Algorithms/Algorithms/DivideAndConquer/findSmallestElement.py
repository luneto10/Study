def smallestElement(arr, left, right):
    if left == right:
        return arr[left]

    mid = (right + left) // 2

    smallest_1 = smallestElement(arr, left, mid)
    smallest_2 = smallestElement(arr, mid + 1, right)

    if smallest_1 < smallest_2:
        return smallest_1

    return smallest_2


def smallestDifference(arr, k, left, right):
    if left == right:
        return arr[left]

    mid = (right + left) // 2

    smallest_1 = smallestDifference(arr, k, left, mid)
    smallest_2 = smallestDifference(arr, k, mid + 1, right)

    if abs(smallest_1 - k) < abs(smallest_2 - k):
        return smallest_1

    return smallest_2


array = [1, 20, 5, -1, 3, 40, -2, 20]
print(smallestElement(array, 0, len(array) - 1))
