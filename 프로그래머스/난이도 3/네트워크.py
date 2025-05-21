# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def dfs(net, node, visited):
    visited.add(node)
    for next_node in range(len(net[node])):
        if net[node][next_node] == 0 or next_node in visited: continue
        dfs(net, next_node, visited)
    
def solution(n, computers):
    answer = 0
    visited = set()
    for node in range(n):
        if node in visited: continue
        dfs(computers, node, visited)
        answer += 1
    return answer