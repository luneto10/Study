sorted_list = [2, 4, 5, 6, 10, 92, 100, 123]


def binary_search(list_search: list, key):
    L = 0
    R = len(list_search) - 1
    while L <= R:
        middle_idx = (R + L) // 2
        middle_element = list_search[middle_idx]
        if middle_element < key:
            L = middle_idx + 1
        elif middle_element > key:
            R = middle_idx - 1
        else:
            return middle_idx
    return -1

def binary_serach_recursive(list_search: list, key, L=0, R=0):
    if L > R:
        return -1
    
    middle_idx = (R + L) // 2
    middle_element = list_search[middle_idx]
    if middle_element < key:
        return binary_serach_recursive(list_search, key, middle_idx + 1, R)
    elif middle_element > key:
        return binary_serach_recursive(list_search, key, L, middle_idx - 1)
    else:
        return middle_idx


# print(binary_search(sorted_list, 2))
