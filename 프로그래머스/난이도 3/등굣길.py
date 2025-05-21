# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0
    puddles = set(map(tuple, puddles))
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    dp[1][0] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if (i, j) in puddles: dp[i][j] = 0
            else: dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
    return dp[m][n]