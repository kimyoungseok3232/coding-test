# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0
    
    num = []
    
    while storey != 0:
        num.append(storey%10)
        storey = int(storey/10) 
    num.append(0)
    check = 0
    for i in range(len(num)):

        if num[i] < 5:
            answer += num[i]
            
        elif num[i] == 5:
            if num[i+1] < 5:
                answer += num[i]
            else:
                answer += 10-num[i]
                num[i+1] += 1
        else:
            answer += 10-num[i]
            num[i+1] += 1
            
    return answer