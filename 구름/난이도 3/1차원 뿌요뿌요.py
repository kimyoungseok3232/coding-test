# https://level.goorm.io/exam/49076/1차원-뿌요뿌요/quiz/1
n, m = map(int,input().split())
board = input()+' '
res = ['',board[0]]
count = [1]

for i in range(1,n+1):
	if res[-1] != board[i] and count[-1] >= m:
		cnt = count.pop()
		for _ in range(cnt):
			res.pop()

	if res[-1] != board[i]:
		count.append(0)
				
	res.append(board[i])
	count[-1] += 1

if len(res) > 2:
	print(''.join(res))
else:
	print('CLEAR!')