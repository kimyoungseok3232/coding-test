# https://level.goorm.io/exam/170813/두-실수-더하기/quiz/1
a, b = input().split()
up = 0
sumstr = ''
if len(a) == len(b) == 8:
	for i in range(-1,-9,-1):
		if a[i] != '.' and b[i] != '.':
			s = int(a[i])+int(b[i])+up
			up = s//10
			sumstr += str(s%10)
		else: sumstr += '.'
	if up : sumstr += str(up)
	print(sumstr[::-1])
elif len(a) != len(b):
	for i in range(-1,-9,-1):
		if a[i] != '.' and b[i] != '.':
			s = int(a[i])+int(b[i])+up
			up = s//10
			sumstr += str(s%10)
		else: sumstr += '.'
	sumstr += str(up+1)
	print(sumstr[::-1])
else:
	print('20.000000')