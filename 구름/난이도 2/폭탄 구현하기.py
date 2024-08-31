# https://level.goorm.io/exam/159666/폭탄-구현하기/quiz/1
n,k = map(int,input().split())
ans = 0

if n == 1:
	ans = k
else:
	for i in range(k):
		low, col = map(int,input().split())
		ans += 5
		if low == 1 or low == n: ans -= 1
		if col == 1 or col == n: ans -= 1

print(ans)