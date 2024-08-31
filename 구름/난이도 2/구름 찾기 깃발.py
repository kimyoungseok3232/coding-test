# https://level.goorm.io/exam/195689/구름-찾기-깃발/quiz/1
N, K = map(int,input().split())

board = [[0 for i in range(N+2)]]
flag = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(N):
	board.append([0] + list(map(int,input().split())) + [0])
board.append([0 for i in range(N+2)])

for i in range(1,N+1):
	for j in range(1,N+1):
		if board[i][j] == 0:
			tmp = sum(board[i-1][j-1:j+2])+sum(board[i][j-1:j+2])+sum(board[i+1][j-1:j+2])
			flag[tmp] += 1
			
print(flag[K])