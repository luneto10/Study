def subsets(nums: int):
    n = len(nums)
    res, sol = [[]], []
    visited = set()

    def backtrack(i):
        if i == n:
            return

        # Pick nums[i]
        sol.append(nums[i])
        if tuple(sol) not in visited:
            visited.add(tuple(sol[:]))
            res.append(sol[:])
        backtrack(i + 1)
        sol.pop()

        # Dont Pick nums[i]
        backtrack(i + 1)

    backtrack(0)
    return res


power = subsets([1, 2, 3, 4, 5])
print(len(power))
for subset in power:
    print(subset)
