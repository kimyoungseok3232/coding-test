# https://school.programmers.co.kr/learn/courses/30/lessons/64064

def dfs(banned_id, count, st = 0, visited = set(), answer = set()):
    if len(visited) == len(banned_id): 
        answer.add(tuple(sorted(list(visited))))
        return 0
    
    for user in count[banned_id[st]]:
        if user in visited: continue
        visited.add(user)
        dfs(banned_id, count, st+1, visited, answer)
        visited.remove(user)

def solution(user_id, banned_id):
    answer = set()
    count = {val:[] for val in banned_id}
    
    for user in user_id:
        for ban in set(banned_id):
            if len(user) == len(ban):
                for idx in range(len(user)):
                    if ban[idx] == '*' or user[idx] == ban[idx]: continue
                    break
                else: count[ban].append(user)

    dfs(banned_id, count, answer = answer)
    
    return len(answer)