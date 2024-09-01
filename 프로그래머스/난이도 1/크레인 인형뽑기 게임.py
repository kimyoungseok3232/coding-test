# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    last = [0]
    for move in moves:
        for row in board:
            if row[move-1] == 0: continue
            elif last[-1] != row[move-1]: last.append(row[move-1])
            else: answer+=2; last.pop()
            row[move-1] = 0
            break
    return answer