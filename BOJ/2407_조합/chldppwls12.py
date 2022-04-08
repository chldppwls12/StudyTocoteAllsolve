from sys import  stdin
input = stdin.readline

n, m = map(int, input().split())

def solution():
  memo = [[0]*101 for _ in range(101)]
  for i in range(1, 101):
    memo[i][0] = 1
    memo[i][i] = 1
  
  for i in range(2, 101):
    for j in range(1, i):
      memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

  return memo[n][m]

print(solution())