N = int(input()) #input
#DP
d = [0] * 1000001 #count
#bottom-up 
for i in range(2, N+1): 
    d[i] = d[i-1] + 1 #-1
    if i%2==0: #/2
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0: #/3
        d[i] = min(d[i], d[i//3]+1)
print(d[N])