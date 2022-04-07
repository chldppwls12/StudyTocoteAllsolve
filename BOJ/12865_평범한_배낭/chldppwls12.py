from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
wv = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

def solution():
  memo = [[0]* (K+1) for _ in range(N+1)]
  for i in range(1, N+1):
    for j in range(1, K+1):
      w = wv[i][0]
      v = wv[i][1]

      if j < w:
        memo[i][j] = memo[i-1][j]
      else:
        memo[i][j] = max(v + memo[i-1][j-w], memo[i-1][j])
  
  return memo[N][K]

print(solution())