# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = [[0,i+1] for i in range(N+1)]
    
    for st in stages: answer[st-1][0] += 1

    clear = len(stages)
    
    for i in range(N):
        if clear:
            answer[i][0], clear = answer[i][0]/(answer[i][0]+clear), clear-answer[i][0]
    
    answer = list(zip(*sorted(answer[:-1],key = lambda x:(-x[0]))))[1]
    
    return answer