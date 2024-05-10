
n, m = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

l = 0
r = h[n-1]
while(l<=r):
    mid = (l+r)//2
    home = 0
    for i in h:
        if i > mid:
            home+=i-mid
    if home >= m:
        l = mid+1
    else:
        r = mid-1

print(r)

