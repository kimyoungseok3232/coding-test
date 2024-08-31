# https://level.goorm.io/exam/88520/놀이공원/quiz/1
user_input = int(input())
for _ in range(user_input):
	N, K = map(int,input().split())
	min_wastes = 10000
	loop_size = N-K+1

	land = []
	for n in range(N):
		land.append(list(map(int,input().split())))
	
	mat1 = []
	for i in range(loop_size):
		mat1.append([])
		for j in range(N):
			mat1[i].append(sum(land[j][i:i+K]))
	
	for i in range(loop_size):
		for j in range(loop_size):
			tmp = sum(mat1[i][j:j+K])
			if tmp < min_wastes:
				min_wastes = tmp
	
	print(min_wastes)
