# https://level.goorm.io/exam/49101/환경과-쥐-크기의-상관관계/quiz/1

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_d = {}
b_d = {}

for i in a:
	for j in range(-2,3):
		if i+j in a_d:
			a_d[i+j] += 1
		else:
			a_d[i+j] = 1

for i in b:
	for j in range(-2,3):
		if i+j in b_d:
			b_d[i+j] += 1
		else:
			b_d[i+j] = 1

a_max = max(a_d, key = lambda x: (a_d[x],-x))
b_max = max(b_d, key = lambda x: (b_d[x],-x))
print(a_max, b_max)
if a_max > b_max:
	print('good')
else:
	print('bad')