# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    A.sort()
    B.sort()
    answer = len(A)
    count = 0
    for i in range(len(B)):
        if B[i] > A[i-count]: continue
        count += 1
            
    return answer-count