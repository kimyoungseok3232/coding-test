# https://level.goorm.io/exam/174924/연속-점수/quiz/1
n = int(input())

prob = list(map(int,input().split()))

score = []

score.append(prob[0])

for i in range(1,n):
	if prob[i-1]+1 == prob[i]:
		score[-1] += prob[i]
	else:
		score.append(prob[i])
		
print(max(score))
