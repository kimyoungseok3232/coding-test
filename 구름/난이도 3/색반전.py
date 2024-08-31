# https://level.goorm.io/exam/43076/1c-색-반전/quiz/1
n = int(input())
board = [[0 for i in range(4200)] for i in range(4200)]
for i in range(n):
	q = int(input())
	sq = 0
	for j in range(q):
		x, y, l = map(int,input().split())
		x, y = x + y, x - y
		for rx in range(x-l,x+l):
			for ry in range(y-l,y+l):
				if board[rx][ry] == i+1:
					board[rx][ry] = 0
					sq -= 1
				else:
					board[rx][ry] = i+1
					sq += 1
	print(sq//2)