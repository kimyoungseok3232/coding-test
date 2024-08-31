# https://level.goorm.io/exam/175909/카드-모으기/quiz/1

# n, m = map(int,input().split())

# card = set()
# res = 0
# while len(card) != n and res < m:
# 	c = int(input())
# 	res += 1
# 	card.add(c)

# if len(card) == n:
# 	print(res)
# else:
# 	print(-1)

n, m = map(int,input().split())

card = [True for i in range(n)]
res, tmp = 0, 0
while res != m:
	c = int(input())-1
	res += 1
	if card[c]:
		tmp += 1
		card[c] = False
		if tmp == n:
			print(res)
			break

else:
	print(-1)