# https://level.goorm.io/exam/43068/1a-인공지능-청소기/quiz/1
user_input = int(input())
for i in range(user_input):
	X, Y, N = map(int,input().split())
	m_dis = abs(X) + abs(Y)

	if m_dis <= N and (m_dis-N)%2 == 0 :
		print("YES")
	else:
		print("NO")