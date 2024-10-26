from typing import List

def powerSet(arr: list, result: list = [], subset: list = [], i=0):
    if i == len(array):
        result.append(subset.copy())
    else:
        powerSet(arr, result, subset + [arr[i]], i + 1)
        powerSet(arr, result, subset, i + 1)
    return result


def generate_subsets_recursive(elements):
    start = 0
    path = []
    def backtrack(start, path):
        # Process the current subset 'path' (e.g., print or store it)
        subsets.append(path[:])  # Make a shallow copy
        for i in range(start, len(elements)):
            # Include elements[i] in the subset
            path.append(elements[i])
            backtrack(i + 1, path)
            # Exclude elements[i] from the subset and backtrack
            path.pop()

    subsets = []
    backtrack(0, [])
    return subsets


array = [1, 2, 3, 4]
# generate_subsets_recursive(array)


# def permutation(arr:list):
#     def permutes(arr: list, permutation: list, used: list, res: List[list]):
#         if len(permutation) == len(arr):
#             res.append(permutation.copy())
#             return 
#         for i in range(len(arr)):
#             if not used[i]:
#                 used[i] = True
#                 permutation.append(arr.copy()[i])
#                 permutes(arr, permutation, used, res)
#                 used[i] = False
#                 permutation.pop()
#         return res
    
#     return permutes(arr, [], [False] * len(arr), [])  

def permute(arr: list):
    if len(arr) == 0:
        return [[]]
    perms = permute(arr[1:])
    res = []
    for p in perms:
        for i in range (len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, arr[0])
            res.append(p_copy)
    return res

def getPermutation(n: int, k: int) -> str:
        arr = [i for i in range(1, n + 1)]

        def permute(arr):
            if len(arr) == 0:
                return [[]]
            perms = permute(arr[1:])
            res = []
            for p in perms:
                for i in range (len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, arr[0])
                    res.append(p_copy)
            return res
        permute(arr)
# print(len(permute(array)))
getPermutation(3, 2)
