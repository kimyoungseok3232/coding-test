# https://level.goorm.io/exam/185060/두-정삼각형/quiz/1

def dif(t1, t2):
	dif = 0
	for i in range(len(t1)):
		for j in range(len(t1[i])):
			if t1[i][j] != t2[i][j]:
				dif += 1
	return dif

def rotate60(t):
	res = []
	for i in range(len(t)):
		tmp = []
		for j in range(len(t[i])):
			tmp.append(t[len(t)-1-j][i-j])
		res.append(tmp)
	return res

def symmetry(t):
	for i in range(len(t)):
		for j in range(len(t[i])//2):
			t[i][j], t[i][-j-1] = t[i][-j-1], t[i][j]
	return t

n = int(input())

tA = []
for i in range(n):
	tA.append(list(map(int,input().split())))
	
tB = []
for i in range(n):
	tB.append(list(map(int,input().split())))

d = [dif(tA,tB)]
	
for i in range(2):
	tA = rotate60(tA)
	d.append(dif(tA,tB))

tA = symmetry(tA)
d.append(dif(tA,tB))

for i in range(2):
	tA = rotate60(tA)
	d.append(dif(tA,tB))
	
print(min(d))