import sys
input = sys.stdin.readline

N = int(input())

cost = []
for i in range(N):
    cost.append(list(map(int, input().split())))

dp = [[0]*3 for i in range(N)]
dp[0] = cost[0] 

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
print(min(dp[N-1]))


