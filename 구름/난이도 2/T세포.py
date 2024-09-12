# https://level.goorm.io/exam/49085/t세포/quiz/1

n = int(input())

bn = bin(n)[2:]
lb = len(bn)

print(bn.count('1'))
for i in range(lb):
	if bn[lb-i-1] == '1':
		print(i, end=' ')

# cell = ''
# ccount = 0
# vcount = 0
# while n:
# 	if n%2:
# 		cell += str(vcount)+' '
# 		ccount += 1
# 	n = n//2
# 	vcount += 1

# print(ccount)
# print(cell)