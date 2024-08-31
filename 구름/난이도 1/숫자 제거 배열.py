# https://level.goorm.io/exam/174805/숫자-제거-배열/quiz/1
n,k = input().split()
st = input().split()
ans = 0
for i in st:
	if k not in i:
		ans += 1
print(ans)
