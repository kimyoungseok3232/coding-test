# https://level.goorm.io/exam/175240/stack/quiz/1
n,k = map(int,input().split())
stack = []
for i in range(n):
	command = input().split()
	
	if command[0] == 'push':
		if len(stack) < k: stack.append(command[1])
		else: print("Overflow")
	
	elif command[0] == 'pop':
		if stack: print(stack.pop())
		else: print("Underflow")