def score(arr, answers):
    cnt = 0
    n = len(answers)
    for i in range(n):
        if answers[i] == arr[i]:
            cnt +=1
    return cnt

def solution(answers):
    f = [1,2,3,4,5]*(10000//5)
    s = [2,1,2,3,2,4,2,5]*(10000//8)
    t = [3,3,1,1,2,2,4,4,5,5]*(10000//10)
    ans = [score(f, answers), score(s, answers), score(t, answers)]
    k = max(ans)
    answer = []
    for i in range(3):
        if ans[i] == k:
            answer.append(i+1)
    return answer
    
    