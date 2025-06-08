# https://school.programmers.co.kr/learn/courses/30/lessons/389481

def solution(n, bans):
    answer = ''
    a_dict = {chr(i+96):i for i in range(1,27)}
    for i in range(len(bans)):
        tmp = 0
        mul = 1
        for idx, a in enumerate(reversed(bans[i])):
            tmp += mul*a_dict[a]
            mul *= 26
        bans[i] = tmp
        
    bans.sort()
    for ban in bans:
        if ban <= n: n += 1

    while n:
        n -= 1
        answer = chr(97 + n % 26) + answer
        n //= 26

    return answer