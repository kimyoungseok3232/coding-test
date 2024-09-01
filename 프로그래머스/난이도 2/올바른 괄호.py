# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    
    num1 = 0
    num2 = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            num1 += 1
        elif s[i] == ')':
            num2 += 1
        
        if num1 < num2:
            answer = False
            break
    
    if num1 != num2:
        answer = False
    
    return answer