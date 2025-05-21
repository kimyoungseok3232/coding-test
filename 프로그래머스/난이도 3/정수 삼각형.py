# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    dp = [[triangle[0][0]]]
    for height in range(1, len(triangle)):
        dp.append([])
        dp[height].append(dp[height-1][0]+triangle[height][0])
        for idx in range(1, height):
            dp[height].append(max(dp[height-1][idx-1],dp[height-1][idx])+triangle[height][idx])
        dp[height].append(dp[height-1][height-1]+triangle[height][height])
    return max(dp[-1])