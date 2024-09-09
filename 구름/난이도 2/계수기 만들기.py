# https://level.goorm.io/exam/43061/계수기-만들기/quiz/1

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
k = int(input())

res = ''

for i in range(1,len(A)+1):
	res = str((k+B[-i])%(A[-i]+1))+res
	k = (k+B[-i])//(A[-i]+1)

print(res)