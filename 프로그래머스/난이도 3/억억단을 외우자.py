# https://school.programmers.co.kr/learn/courses/30/lessons/138475

def solution(e, starts):
    answer = []
    
    divisor = [1]*(e+1)
    for i in range(2, e+1):
        for j in range(i, e+1, i):
            divisor[j] += 1    
            
    ss = sorted(starts)
    ans_dict = {}
    idx = 0
    for i in ss:
        if i > idx:
            tmp = divisor[i:]
            idx = tmp.index(max(tmp))+i
        ans_dict[i] = idx

    for i in starts:
        answer.append(ans_dict[i])

    return answer