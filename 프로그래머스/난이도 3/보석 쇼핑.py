# https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    type_count = len(set(gems))
    gem_count = {}
    count = 0
    st = 0
    answer = [1, len(gems)]
    for idx in range(len(gems)):
        gem_count[gems[idx]] = tmp = gem_count.get(gems[idx], 0) + 1
        if tmp == 1: count += 1
        
        for idx2 in range(st, len(gems)):
            if gem_count[gems[idx2]] == 1: break
            st += 1
            gem_count[gems[idx2]] -= 1
            
        if count == type_count and answer[1] - answer[0] > idx - st:
            answer[0], answer[1] = st+1, idx+1
        
    return answer