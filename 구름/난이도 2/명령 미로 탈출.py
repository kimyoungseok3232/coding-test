# https://level.goorm.io/exam/210125/명령-미로-탈출/quiz/1
n,k = map(int,input().split())
move = input()
board = [[3 for i in range(n+2)]]
for i in range(n):
	board.append([3] + list(map(int,input().split())) + [3])
board.append([3 for i in range(n+2)])

st, ed = [], []

for i in range(1,n+1):
	for j in range(1,n+1):
		if st and ed:
			break
		if board[i][j] == 1:
			st = [i,j]
		if board[i][j] == 2:
			ed = [i,j]

cnt = 0
for i in move:
	cnt += 1
	if i == 'U' and board[st[0]-1][st[1]] != 3:
		st[0] -= 1
	elif i == 'D' and board[st[0]+1][st[1]] != 3:
		st[0] += 1
	elif i == 'L' and board[st[0]][st[1]-1] != 3:
		st[1] -= 1
	elif i == 'R' and board[st[0]][st[1]+1] != 3:
		st[1] += 1
	else:
		cnt -= 1

	if st == ed:
		print('SUCCESS', cnt)
		break
if st != ed:
	print('FAIL')
