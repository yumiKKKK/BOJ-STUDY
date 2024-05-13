n = int(input())
inputs = list(map(int, input().split()))

arr = sorted(set(inputs))

dic = {arr[i]: i for i in range(len(arr))}

for i in inputs:
    print(dic[i], end = " ")
