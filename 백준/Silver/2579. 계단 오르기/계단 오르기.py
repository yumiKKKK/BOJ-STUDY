
num = int(input())
dp = [0] * (num+1)
scores = [0] * (num+1)
for i in range(1, num+1):
    scores[i] = int(input())
    
if num == 1:
    print(scores[1])
    exit()
elif num == 2:
    print(sum(scores[:3]))
    exit()
dp[1] = scores[1]
dp[2] = scores[1] + scores[2]

for i in range(3, num+1):
    dp[i] = max(scores[i] + dp[i-2], scores[i]+scores[i-1]+dp[i-3])

print(dp[-1])