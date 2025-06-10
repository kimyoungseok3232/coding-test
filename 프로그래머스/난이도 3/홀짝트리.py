# https://school.programmers.co.kr/learn/courses/30/lessons/388354

def solution(nodes, edges):
    answer = [0, 0]
    tree = {node:[] for node in nodes}
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
        
    visited = set()
    for node in nodes:
        if node in visited: continue
        q = tree[node].copy()
        visited.add(node)
        tmp = node % 2 == len(tree[node]) % 2
        count = 1
        while q:
            n = q.pop()
            count += 1
            tmp += n % 2 == len(tree[n]) % 2
            visited.add(n)
            q.extend(i for i in tree[n] if i not in visited)
        if tmp == 1: answer[0] += 1
        if tmp == count-1: answer[1] += 1
            
        
    return answer