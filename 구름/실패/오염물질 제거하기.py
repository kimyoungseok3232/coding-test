# https://level.goorm.io/exam/43081/1e-오염물질-제거하기/quiz/1
# 임의로 추가한 모든 테스트 케이스에서는 정상 동작하였으나 제출시 실패
# 어떤 조건에서 실패하는지 확인 필요
from collections import defaultdict
t = int(input())
for _ in range(t):
	n = int(input())
	point = []
	for _ in range(n):
		x, y = map(int,input().split())
		point.append((x,y))
	
	res = 1
	for l in range(n):
		line_dict = defaultdict(lambda: 1)
		for k in range(n):
			p1,p2 = point[l], point[k]
			if p1 == p2:
				continue
			if p1[0] == p2[0]:
				coe = 'inf'
			else:
				coe = (p1[1]-p2[1])/(p1[0]-p2[0])
			line_dict[coe] += 1
			res = max(line_dict[coe],res)

	print(res)