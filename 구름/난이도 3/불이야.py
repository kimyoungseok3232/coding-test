# https://level.goorm.io/exam/49051/불이야/quiz/1
from collections import deque
r,c = map(int,input().split())

room = ['#'*(c+2)]
for i in range(r):
	room.append('#'+input()+'#')
room.append('#'*(c+2))

goorm = deque()
visited = set()

for i in range(1,r+1):
	if goorm: break
	for j in range(1,c+1):
		if room[i][j] == '&': 
			goorm.append((0,i,j))
			visited.add((i,j))
			break

dxy = [(-1,0),(1,0),(0,-1),(0,1)]

flag = 1
while goorm and flag:
	nn = goorm.popleft()
	t = nn[0]
	
	for x,y in dxy:
		low, col = nn[1]+x, nn[2]+y
		loc = (low,col)
		mark = room[low][col]
		if loc in visited or mark == '#': continue
		elif mark == '@': 
			flag = 0
			break
		visited.add(loc)
		element = (t+1,low,col)
		goorm.append(element)

if flag: print(-1)
else: print(t)