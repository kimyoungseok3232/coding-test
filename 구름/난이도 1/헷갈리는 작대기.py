# https://level.goorm.io/exam/47882/헷갈리는-작대기/quiz/1
user_input = input()
num1 = 0
numI = 0
numl = 0
num = 0
for i in user_input:
	if i == '1':
		num1 += 1
	elif i == 'I':
		numI += 1
	elif i == 'l':
		numl += 1
	elif i == '|':
		num += 1

print(num1)
print(numI)
print(numl)
print(num)
		