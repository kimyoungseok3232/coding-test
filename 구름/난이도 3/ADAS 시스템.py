# https://level.goorm.io/exam/152116/현대모비스-예선-adas-시스템/quiz/1
w, h = map(int,input().split())
board = ['W'*(h+2)]
for i in range(w):
	board.append('W'+input()+'W')
board.append('W'*(h+2))
st = []
for i in range(1,w+1):
	if st: break
	for j in range(1,h+1):
		if board[i][j] == 'S': 
			st = ('S',i,j,0)
			break

import heapq
visited = set()
visited.add(('S',st[1],st[2]))
move = [st]
d = [(-1,0),(0,-1),(0,1),(1,0)]
res, state = 0, 1

while state:
	now = heapq.heappop(move)
	low, col = now[1], now[2]
	res += now[3]
	for x,y in d:
		l, c = low+x, col+y
		m = board[l][c]
		velement = (m,l,c)
		sc = 0
		if velement in visited or m == 'W': continue
		elif m == 'P': sc = -4
		elif m == '0' : m = 'Z'
		elif m == 'E' : 
			state = 0
			break
		
		for i in range(l-1,l+2):
			for j in range(c-1,c+2):
				if board[i][j] == 'P': sc += 1

		element = (m,l,c,sc)
		heapq.heappush(move,element)
		visited.add(velement)

print(max(0,res))
