from collections import deque
# def partition_equal_sum(arr):
#     # If total sum is odd, partitioning into two equal subsets is not possible
#     total_sum = sum(arr)
#     if total_sum % 2 != 0:
#         return None
    
#     # Call the recursive function
#     return find_partition(arr, 0, [], [], 0, 0)

# def find_partition(arr, idx, subset1, subset2, sum1, sum2):
#         # Base case: if we've gone through all elements
#         if idx == len(arr):
#             # If the sums of both subsets are equal, return them
#             if sum1 == sum2:
#                 return subset1, subset2
#             else:
#                 return None
        
#         # Choose the current element for subset1
#         result = find_partition(arr, idx + 1, subset1 + [arr[idx]], subset2, sum1 + arr[idx], sum2)
#         if result:
#             return result
        
#         # Choose the current element for subset2
#         result = find_partition(arr, idx + 1, subset1, subset2 + [arr[idx]], sum1, sum2 + arr[idx])
#         return result


# # Example usage
# arr = [1, 2, 3, 4]
# result = partition_equal_sum(arr)
# if result:
#     print(f"Subset 1: {result[0]}, Subset 2: {result[1]}")
# else:
#     print("No partition exists.")
    
def water_jug(jug1, jug2, target: int):
    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    parents = {}
    while queue:
        current_state = queue.popleft()
        amt1, amt2 = current_state
        
        if amt1 == target or amt2 == target:
            steps = []
            while current_state != (0,0):
                steps.append(current_state)
                current_state = parents[current_state]
            steps.append((0, 0))
            steps.reverse()
            return steps
        
        next_states = [
            (jug1, amt2),  
            (amt1, jug2),  
            (0, amt2),     
            (amt1, 0),     
            (min(jug1, amt1 + amt2), max(0, amt1 + amt2 - jug1)),  
            (max(0, amt1 + amt2 - jug2), min(jug2, amt1 + amt2))   
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                parents[state] = current_state

    return None

x = water_jug(1,2,3)
print(x) 

def find_partition(arr: set):
    listsub = list(arr)
    subsets = []
    for i in range(2 ** len(listsub)):
        subset = set()
        for k in range(len(listsub)):
            if i & 1 << k:
                subset.add(listsub[k])
        subsets.append(subset)
        
    for subset in subsets:
        if sum(subset) == sum(arr - subset):
            return (subset, arr - subset)
    return None

print(find_partition({1, 5, 5, 11}))