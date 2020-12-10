from input import input

xs = input
xs.append(0)
xs = sorted(input)
xs.append(max(xs) + 3)

DP = {}


def solve_step2(i):
    if i == len(xs) - 1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(xs)):
        if xs[j]-xs[i] <= 3:
            ans += dp(j)
    DP[i] = ans
    return ans


result_step2 = solve_step2(0)
print(result_step2)
