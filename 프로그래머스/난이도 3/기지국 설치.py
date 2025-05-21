# https://school.programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    answer = 0
    last = 1
    stations.append(n+w+1)
    for station in stations:
        answer += 1+(station-w-last-1)//(2*w+1)
        last = station+w+1
    return answer