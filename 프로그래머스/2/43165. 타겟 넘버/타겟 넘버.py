cnt = 0
def dfs(idx, res, numbers, target, state):
    global cnt
    if idx == len(numbers):
        if res == target:
            cnt += 1
        return
    dfs(idx + 1, res + numbers[idx], numbers, target, "+")
    dfs(idx + 1, res - numbers[idx], numbers, target, "-")
def solution(numbers, target):
    idx, res = 0, 0
    dfs(idx, res, numbers, target, "")
    return cnt