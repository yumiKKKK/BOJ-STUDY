import sys
input = sys.stdin.readline

n = int(input())
num = 4
def func(n, cnt):
    global num
    if n==0:
        num = min(num, cnt)
        return
    if cnt > num:
        return
    for i in range(int(n**0.5), int((n//(4-cnt))**0.5), -1):
        func(n-i**2, cnt+1)
    
func(n, 0)
print(num)