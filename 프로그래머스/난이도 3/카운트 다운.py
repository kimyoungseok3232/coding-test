# https://school.programmers.co.kr/learn/courses/30/lessons/131129

def solution(target):
    
    answer = []
    
    score = [i for i in range(20,0,-1)] + [i*2 for i in range(20,0,-1)] + [i*3 for i in range(20,0,-1)] + [50]
    
    score = list(reversed(list(set(score))))
    
    min_score = target
    idx = 0
    score_dict = [{target:0}]
    
    while min_score > 0:
        score_dict.append({})

        for i in score_dict[idx]:
            for j in score:
                tmp = i-j
                if tmp - min_score > -1:
                    break
                    
                if tmp >= 0:
                    if j < 21 or j == 50:
                        if tmp in score_dict[idx+1] and score_dict[idx+1][tmp] >= score_dict[idx][i]+1:
                            continue
                        else:
                            score_dict[idx+1][tmp] = score_dict[idx][i]+1
                    else:
                        if tmp in score_dict[idx+1] and score_dict[idx+1][tmp] >= score_dict[idx][i]:
                            continue
                        else:
                            score_dict[idx+1][tmp] = score_dict[idx][i]

                    

        idx += 1
        min_score = min(score_dict[idx].keys())


    answer.append(len(score_dict)-1)
    answer.append(score_dict[idx][0])
    
    return answer