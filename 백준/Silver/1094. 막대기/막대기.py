X = int(input())

dp = [64]

while sum(dp) != X:
    num = dp.pop(-1)
    dp.append(num // 2)
    if sum(dp) < X:
        dp.append(num // 2)
print(len(dp))