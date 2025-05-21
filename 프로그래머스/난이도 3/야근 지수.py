# https://school.programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    answer = 0
    works.sort()
    count = 1
    
    while n and len(works) > 1:
        if works[-1] == works[-2]: 
            works.pop()
            count += 1
        elif n >= count * (works[-1] - works[-2]):
            n -= count * (works[-1] - works[-2])
            works.pop()
            count += 1
        else: break

    if works[-1] >= n // count:
        works[-1] -= n // count
        n -= count * (n // count)
        
    if count > n:
        if n and works[-1] > 0:
            count1 = n
            count2 = count - n
            answer += count1 * (works[-1]-1)**2
            answer += count2 * (works[-1])**2
        else:
            answer += count * (works[-1])**2
    works.pop()
    
    for work in works:
        answer += work*work
    
    return answer