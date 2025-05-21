# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    last = -30001
    for st, ed in routes:
        if st > last:
            last = ed
            answer += 1
    return answer