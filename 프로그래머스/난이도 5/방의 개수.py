# https://school.programmers.co.kr/learn/courses/30/lessons/49190

def solution(arrows):
    answer = 0
    
    visited = {}
    edge = {}
    
    move = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    
    now = 0,0

    visited[f"{now}"] = 1
    
    for arrow in arrows:
        
        checker = 0
        
        next = now[0]+move[arrow][0],now[1]+move[arrow][1]
        
        if visited.get(f"{next}") == None:
            visited[f"{next}"] = 1
        else:
            checker = 1
        
        if edge.get(f"{now},{next}") == None:
            edge[f"{now},{next}"] = 1
            edge[f"{next},{now}"] = 1
            if checker == 1:
                answer += 1
        
        now = next
        
        checker = 0
        
        next = now[0]+move[arrow][0],now[1]+move[arrow][1]
        
        if visited.get(f"{next}") == None:
            visited[f"{next}"] = 1
        else:
            checker = 1
        
        if edge.get(f"{now},{next}") == None:
            edge[f"{now},{next}"] = 1
            edge[f"{next},{now}"] = 1
            if checker == 1:
                answer += 1
        
        now = next

    print(next)

    return answer