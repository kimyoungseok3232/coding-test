# https://school.programmers.co.kr/learn/courses/30/lessons/12953

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(arr):
    
    
    answer = 1
    
    for i in arr:
        answer = lcm(answer,i)
    
    return answer