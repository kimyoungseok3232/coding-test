# https://level.goorm.io/exam/51352/비타민-주스/quiz/1

n = int(input())

dic = {}
for i in range(n):
	price, vitamin = input().split()
	price, vitamin = int(price), ''.join(sorted(list(vitamin)))
	
	if vitamin not in dic or dic[vitamin] > price:
		dic[vitamin] = price

res = []
tmp = [['ABC'], ['AB','C'], ['AB','AC'], ['AB','BC'], ['AC','B'],['AC','BC'], ['BC','A'], ['A','B','C']]

for i in tmp:
	p = 0
	for j in i:
		if j in dic: p += dic[j]
		else: break
	else: res.append(p)

if res:
	print(min(res))
else:
	print(-1)