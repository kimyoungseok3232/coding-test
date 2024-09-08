# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    answer = ''
    x_c = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    y_c = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    
    for l in X:
        x_c[l] += 1
    
    for l in Y:
        y_c[l] += 1
    
    for i in range(9,-1,-1):
        answer += str(i) * min(x_c[str(i)],y_c[str(i)])
    
    if answer and answer[0] != "0":
        return answer
    elif answer:
        return "0"
    return "-1"