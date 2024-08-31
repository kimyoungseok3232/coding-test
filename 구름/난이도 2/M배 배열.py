# https://level.goorm.io/exam/174909/m배-배열/quiz/1
N, M = map(int,input().split())

line = map(int,input().split())

for i in line:
	if i % M != 0 :
		i *= M
	print(i,end=' ')