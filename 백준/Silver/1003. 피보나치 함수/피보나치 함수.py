t = int(input())
for i in range(t):
    c0, c1 = 1, 0   
    n = int(input())
    for i in range(n):
        c0, c1 = c1, c0+c1
    print(c0, c1)