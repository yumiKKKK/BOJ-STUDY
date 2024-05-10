n, m = map(int, input().split())
hear = set(input() for i in range(n))
see = set(input() for i in range(m))
result = sorted(list(hear&see))
print(len(result))
for i in result:
    print(i)