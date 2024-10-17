n = int(input())
room = [list(map(int,input().split())) for _ in range(n)]
cases = [[[0 for _ in range(n)]for _ in range(n)]for _ in range(3)]
cases[0][0][1] = 1
for i in range(n):
    for j in range(2,n):
        if room[i][j] == 0: 
            cases[0][i][j] = cases[0][i][j-1] + cases[2][i][j-1]
            cases[1][i][j] = cases[1][i-1][j] + cases[2][i-1][j]
        if room[i][j] == 0 and room[i-1][j] == 0 and room[i][j-1] == 0:
            cases[2][i][j] = cases[0][i-1][j-1] + cases[1][i-1][j-1] + cases[2][i-1][j-1]
res = cases[0][n-1][n-1]+cases[1][n-1][n-1]+cases[2][n-1][n-1]
print(res)