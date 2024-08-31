# https://level.goorm.io/exam/175241/queue/quiz/1
N, K = map(int, input().split())

que = []
for _ in range(N):
	order = list(input().split())
	if order[0] == 'push':
		print('Overflow') if len(que) == K else que.append(order[-1])
	else:
		print('Underflow') if len(que) == 0 else print(que.pop(0))