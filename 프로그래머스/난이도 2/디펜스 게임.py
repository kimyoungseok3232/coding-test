# https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq

def solution(n, k, enemy):
    answer = 0
    
    e_num = 0
    last_big = 0
    heap = []
    check = 0
    for i in range(len(enemy)):
        e_num += enemy[i]
        heapq.heappush(heap,-enemy[i])
        if e_num > n:
            if k > 0:
                k-=1
                e_num += heapq.heappop(heap)
            else:
                break
        answer+=1

    return answer