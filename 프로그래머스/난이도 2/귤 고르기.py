# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    
    answer = 0
    
    counter = sorted(list(dict(Counter(tangerine)).values()),reverse=True)
    
    for i in counter:
        if k > i:
            k -= i
            answer += 1
        else:
            answer += 1
            break

    return answer