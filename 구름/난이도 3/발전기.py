# https://level.goorm.io/exam/195694/발전기/quiz/1
N = int(input())

town = []
elec = 0

for _ in range(N):
	town.append(input().split())

def bfs(low,col):
	q = [(low,col)]
	while q:
		l, c = q.pop()
		town[l][c] = '0'
		up = l-1 if l>0 else l
		down = l+1 if l<N-1 else l
		left = c-1 if c>0 else c
		right = c+1 if c<N-1 else c
		
		if town[up][c] == '1':
			q.append((up,c))
		if town[down][c] == '1':
			q.append((down,c))
		if town[l][left] == '1':
			q.append((l,left))
		if town[l][right] == '1':
			q.append((l,right))

for i in range(N):
	for j in range(N):
		if town[i][j] == '1':
			bfs(i,j)
			elec += 1


print(elec)