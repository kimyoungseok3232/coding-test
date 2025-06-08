# https://school.programmers.co.kr/learn/courses/30/lessons/389481

def solution(n, bans):
    answer = ''
    a_dict = {chr(i+96):i for i in range(1,27)}
    ban_int = []
    for ban in bans:
        tmp = 0
        mul = 1
        for idx, a in enumerate(reversed(ban)):
            tmp += mul*a_dict[a]
            mul *= 26
        ban_int.append(tmp)
        
    ban_int.sort()
    for ban in ban_int:
        if ban <= n: n += 1

    while n:
        n -= 1
        answer = chr(97 + n % 26) + answer
        n //= 26

    return answer