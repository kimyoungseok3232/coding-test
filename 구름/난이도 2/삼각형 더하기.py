# https://level.goorm.io/exam/195147/삼각형-더하기/quiz/1
n, q = map(int,input().split())
score = []
for i in range(n):
	score.append(list(map(int,input().split())))


for i in range(q):
	t = list(map(int,input().split()))
	list_tmp = [[t[0]-1,t[1]-1], [t[2]-1,t[3]-1], [t[4]-1,t[5]-1]]
	list_tmp.sort()
	
	yst = list_tmp[0][0]
	yed = list_tmp[2][0]
	
	if list_tmp[0][0] == list_tmp[1][0]:
		vy = -1
	else:
		vy = 1
		
	list_tmp.sort(key=lambda x:x[1])
	xst = list_tmp[0][1]
	xed = list_tmp[2][1]
	
	if list_tmp[0][1] == list_tmp[1][1]:
		vx = -1
	else:
		vx = 1
		
	length = yed - yst + 1
	tsum = 0
	
	for j in range(length):
		if vy == -1 and vx == -1:
			tsum += sum(score[yst+j][xst:xed-j+1])
		elif vy == -1 and vx == 1:
			tsum += sum(score[yst+j][xst+j:xed+1])
		elif vy == 1 and vx == -1:
			tsum += sum(score[yst+j][xst:xst+j+1])
		elif vy == 1 and vy == 1:
			tsum += sum(score[yst+j][xed-j:xed+1])
	print(tsum)		
