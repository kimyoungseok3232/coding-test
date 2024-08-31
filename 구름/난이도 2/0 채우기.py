# https://level.goorm.io/exam/175011/0-채우기/quiz/1
user_input = int(input())

board = []
sumij = 0
for i in range(user_input):
	board.append(list(map(int,input().split())))

for i in range(user_input):
	for j in range(user_input):
		if board[i][j] == 0:
			sumij = sum(board[i])
			for k in range(user_input):
				sumij += board[k][j]
			break

print(sumij)