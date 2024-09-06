# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = set()
    nextword = deque([[begin,0]])
    now = ''
    
    while now != target and nextword:
        node = nextword.popleft()
        now, t = node[0], node[1]
        for w in words:
            if w in visited: continue
            dif = 0
            for l in range(len(w)): 
                if w[l] != now[l]: dif += 1
            if dif == 1:
                visited.add(w)
                nextword.append([w,t+1])
                
    if now == target:
        return t
    return 0