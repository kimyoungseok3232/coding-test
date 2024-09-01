# https://school.programmers.co.kr/learn/courses/30/lessons/147354

from operator import itemgetter
def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key=itemgetter(0),reverse=True)
    data = sorted(data, key=itemgetter(col-1))
    for i in range(row_begin-1,row_end):
        tmp = 0
        for j in range(len(data[0])):
            tmp += data[i][j]%(i+1)
        answer ^= tmp 
    return answer