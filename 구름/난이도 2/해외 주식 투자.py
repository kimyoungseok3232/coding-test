# https://level.goorm.io/exam/150257/00증권-주식투자자-a/quiz/1

# 리스트만 사용
n = int(input())
stock_list = []
for i in range(1,n+1):
	stock_price, num_of_stock = map(float,input().split())
	stock_list.append([int(stock_price*num_of_stock*10),i])

stock_list.sort(key=lambda x:(-x[0],x[1]))
for i in stock_list:
	print(i[1],end=' ')

# 힙을 이용한 방법
import heapq
n = int(input())
stock_list = []
for i in range(1,n+1):
	v, s = map(float,input().split())
	heapq.heappush(stock_list,[-int(v*s*10),i])

while stock_list:
	print(heapq.heappop(stock_list)[1],end=' ')