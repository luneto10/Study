import math


def largeNumberMultiplication(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))

    mid = n // 2
    a1 = x // (10**mid)
    a0 = x % (10**mid)
    b1 = y // (10**mid)
    b0 = y % (10**mid)

    c2 = largeNumberMultiplication(a1, b1)
    c0 = largeNumberMultiplication(a0, b0)
    c1 = largeNumberMultiplication(a1 + a0, b1 + b0) - c2 - c0

    return (c2 * 10 ** (2 * mid)) + (c1 * 10**mid) + c0


x = 40200033123123123133123123131231313323132131323132132331321341491249194201491912491024012410412491404020003312312312313312312313123131332313213132313213233132134149124919420149191249102401241041249140
y = 40200033123123123133123123131231313323132131323132132331321341491249194201491912491024012410412491404020003312312312313312312313123131332313213132313213233132134149124919420149191249102401241041249140
expect = x * y
print("EXPECTED: " + str(expect))
print("ACTUAl: " + str(largeNumberMultiplication(x, y)))


def min_time_to_cut(N):

    if N == 0:
        return 0

    # Return the minimum
    # unit of time required
    return int(math.log2(N)) + 1


print(min_time_to_cut(100))


def min_cuts(N):
    if N == 1:
        return 0
    left_cuts = min_cuts(N // 2)
    right_cuts = min_cuts((N - N // 2))
    return left_cuts + right_cuts + 1


def min_cuts(N):
    if N <= 1:
        return 0
    return 1 + min_cuts((N + 1) // 2)


print(min_time_to_cut(100))
