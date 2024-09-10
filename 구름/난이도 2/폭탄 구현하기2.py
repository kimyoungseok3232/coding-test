# https://level.goorm.io/exam/195691/폭탄-구현하기-2/quiz/1

def processing(x):
	if x == '#':
		return 0
	elif x == '@':
		return 2
	return 1

def scale(x):
	return int(x)-1

n,k = map(int,input().split())
ans = 0

board = []
for i in range(n):
	board.append(list(map(processing,input().split())))

bomb = []
for i in range(n):
	bomb.append([0 for i in range(n)])

for i in range(int(k)):
	x, y = map(scale,input().split())
	bomb[x][y] += 1

dxy = [(-1,0),(1,0),(0,0),(0,-1),(0,1)]
res = 0
for i in range(n):
	for j in range(n):
		score = 0
		for dx,dy in dxy:
			x, y = i+dx, j+dy
			if x < 0 or y < 0 or x >= n or y >= n: continue
			score += bomb[x][y]
		res = max(res,score*board[i][j])
print(res)