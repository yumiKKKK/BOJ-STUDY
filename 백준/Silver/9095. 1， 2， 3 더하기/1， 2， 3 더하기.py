
def sumNum(k, sum):
    global count
    if sum > n:
        return
    sum += k
    if sum == n:
        count+=1
    sumNum(1, sum)
    sumNum(2, sum)
    sumNum(3, sum)


t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    sumNum(0, 0)
    print(count)