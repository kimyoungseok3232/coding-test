# https://level.goorm.io/exam/191052/블록-게임/quiz/1
n = int(input())
d = input()
s = list(map(int,input().split()))
board = {(0,0):1}
queue = [(0,0)]
move = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
cur = [0,0]
l = len(d)
score = 1

for i in range(l):
	dxy = move[d[i]]
	cur[0] += dxy[0]
	cur[1] += dxy[1]
	loc = (cur[0],cur[1])
	
	while loc in board:
		key = queue.pop()
		score -= board.pop(key)
		
	queue.append(loc)
	board[loc] = s[i]
	score += s[i]
	
print(score)
	