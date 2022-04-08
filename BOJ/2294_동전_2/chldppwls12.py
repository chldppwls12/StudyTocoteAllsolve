from sys import  stdin
input = stdin.readline

n, k = map(int, input().split())
cl = [int(input()) for _ in range(n)]

def solution():
  memo = [10001] * (k+1)
  memo[0] = 0
  for i in range(n):
    for j in range(cl[i], k+1):
      memo[j] = min(memo[j], memo[j-cl[i]]+1)

  if memo[-1] != 10001:
    return memo[-1]
  else:
    return -1

print(solution())