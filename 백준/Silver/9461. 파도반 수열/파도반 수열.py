def P(n):
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    return dp[n]

t = int(input())
for i in range(t):
    n = int(input())
    print(P(n))

