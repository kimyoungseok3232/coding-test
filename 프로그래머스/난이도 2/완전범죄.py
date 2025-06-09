# https://school.programmers.co.kr/learn/courses/30/lessons/389480

def solution(info, n, m):
    answer = 121
    dp = [-1]*m
    dp[0] = 0
    
    for a, b in info:
        for idx in range(m-1,-1,-1):
            if dp[idx] == -1: continue
            if idx+b < m:
                if min(dp[idx], dp[idx+b]) == -1:
                    dp[idx+b] = dp[idx]
                else:
                    dp[idx+b] = min(dp[idx], dp[idx+b])
            dp[idx] += a
    
    for idx in range(m):
        if dp[idx] >= n or dp[idx] == -1: continue
        answer = min(dp[idx], answer)
        
    if answer == 121: return -1
    return answer