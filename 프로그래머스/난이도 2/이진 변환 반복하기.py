# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0,0]
    string = ""
    i=0
    while s!="1":
        for i in range(len(s)):
            if s[i] == '1':
                string += s[i]
        answer[0] += 1
        answer[1] += len(s) - len(string)
        s = str(bin(len(string)))[2:]
        string = ""
        i+=1
    
    return answer