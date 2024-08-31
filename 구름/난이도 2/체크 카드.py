# https://level.goorm.io/exam/160275/체크-카드/quiz/1
def deposit(n, value, res):
	n += value
	while res and n >= res[0]:
		n -= res.popleft()
	return n
def pay(n, value, res):
	if n >= value:
		return n-value
	return n
def reservation(n, value, res):
	if not res and n >= value:
		n -= value
	else:
		res.append(value)
	return n

fun_dict = {'deposit':deposit, 'pay':pay, 'reservation':reservation}
	
from collections import deque
n, m = map(int,input().split())
res = deque()

for i in range(m):
	command, value = input().split()
	value = int(value)
	n = fun_dict[command](n, value, res)
			
print(n)