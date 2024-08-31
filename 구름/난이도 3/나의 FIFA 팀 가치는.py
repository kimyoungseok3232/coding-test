# https://level.goorm.io/exam/208973/나의-fifa-팀-가치는/quiz/1
# heapq 부분 지우고 주석 제거해서 수정하면 리스트만 이용해서 구현 가능
import heapq
n, k = map(int,input().split())
plist = [[0]for i in range(11)]
for i in range(n):
	p, w = map(int,input().split())
	#plist[p-1].append(w)
	heapq.heappush(plist[p-1],-w)

W = 0

for j in plist:
	#j.sort()
	tmp = 0
	mul = 1
	w = 0
	while len(j)>1:
		t1 = -heapq.heappop(j)
		t2 = -j[0]
		dif = t1-t2
		#dif = j[-1]-j[-2]
		s = tmp + dif*mul
		if s < k:
			mul += 1
			tmp = s
			#j.pop()
		else:
			heapq.heappush(j,-t1)
			w = t1-(k-tmp)//mul
			break
	W+=w

print(W)