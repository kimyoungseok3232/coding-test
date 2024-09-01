# https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    answer = 0
    dis = d**2
    for i in range(0,d+1,k):
        y = dis-i**2
        h_y = int(y**(1/2))
        answer += int(h_y/k)+1
        
            
    return answer