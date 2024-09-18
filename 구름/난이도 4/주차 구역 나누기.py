# https://level.goorm.io/exam/160280/주차-구역-나누기/quiz/1

n = int(input())

a = [1,0]

for i in range(2,n+1):
	a[-2], a[-1] = a[-1], ((2*i-1)*a[-1]+a[-2])%100000007

print(a[-1])