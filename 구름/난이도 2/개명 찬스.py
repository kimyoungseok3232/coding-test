# https://level.goorm.io/exam/49069/출석부/quiz/1
name = input()
for i in range(1,len(name)):
	if name[i-1] > name[i]:
		name = name[:i-1] + name[i:]
		break
else:
	name = name[:-1]
print(name)