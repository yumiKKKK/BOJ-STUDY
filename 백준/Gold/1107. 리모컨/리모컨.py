import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
minn=abs(n-100) 
 
if m==0:
    l=set()
    print(min(minn,len(str(n)))) 
    sys.exit()
else:
    l=set(map(int,input().split()))
    

for i in range(1000001):
    i=str(i)
    
    isT=True
    for j in range(len(i)):
        if int(i[j]) in l:
            isT=False
            break
        
    if isT==True: 
        
        minn=min(minn, abs(n-int(i))+len(str(i)))
        
print(minn)    