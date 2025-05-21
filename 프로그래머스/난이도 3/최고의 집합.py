# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if n > s: return [-1]
    div = s//n
    mod = s%n
    answer = [div for i in range(n-mod)] + [div+1 for i in range(mod)]
    return answer