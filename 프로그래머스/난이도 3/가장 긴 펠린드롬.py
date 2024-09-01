# https://school.programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    answer = 1

    for i in range(0,len(s)):
        max_num1 = 1
        j = 1
        
        if i-j == -1 or i+j == len(s):
            continue
            
        while s[i-j] == s[i+j]:
            max_num1 += 2
            j += 1
            if i-j == -1 or i+j == len(s):
                break
                
        max_num2 = 0
        j = 1
        if s[i-j+1] == s[i+j]:
            while s[i-j+1] == s[i+j]:
                max_num2 += 2
                j += 1
                if i-j+1 == -1 or i+j == len(s):
                    break
                
        if max_num1 > answer:
            answer = max_num1
        if max_num2 > answer:
            answer = max_num2
    return answer