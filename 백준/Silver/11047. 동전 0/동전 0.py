n, k = map(int, input().split())
A=[]
for i in range(n):
    A.append(int(input()))
    
count = 0
for i in reversed(range(n)):
    count += k // A[i] #k를 동전으로 나눈 몫
    k %= A[i] #k를 동전으로 나눈 나머지로 계속
print(count)