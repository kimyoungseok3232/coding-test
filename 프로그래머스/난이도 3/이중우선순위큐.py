# https://school.programmers.co.kr/learn/courses/30/lessons/42628

from heapq import heappop, heappush


def solution(operations):
    minheap = []
    maxheap = []
    deleted = set()
    length = 0
    for idx, op in enumerate(operations):
        c, v = op.split()
        v = int(v)
        if c == 'I':
            heappush(minheap, (v, idx))
            heappush(maxheap, (-v, idx))
            length += 1
        elif length > 0:
            if v == 1: 
                tmp = heappop(maxheap)
                while tmp[1] in deleted: tmp = heappop(maxheap)
            else:
                tmp = heappop(minheap)
                while tmp[1] in deleted: tmp = heappop(minheap)
            deleted.add(tmp[1])
            length -= 1
            if length == 0:
                minheap = []
                maxheap = []
                deleted = set()
    
    if length == 0: return [0,0]

    maxv = heappop(maxheap)
    while maxv[1] in deleted: maxv = heappop(maxheap)
    
    minv = heappop(minheap)
    while minv[1] in deleted: minv = heappop(minheap)
    
    return [-maxv[0], minv[0]]