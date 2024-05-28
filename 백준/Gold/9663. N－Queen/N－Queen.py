import sys
input = sys.stdin.readline
N = int(input())

def backtracking(k):
    global cnt
    for i in range(N):
        if queen(k,i): 
            board[k] = i
            if k == N-1: 
                cnt += 1
                return
            else:
                backtracking(k+1)
def queen(a,b): 
    for i in range(a):
        if board[i] == b or abs(board[i]-b) == abs(i-a): 
            return False 
    return True 

board = [0]*N 
cnt = 0
backtracking(0)
print(cnt)
