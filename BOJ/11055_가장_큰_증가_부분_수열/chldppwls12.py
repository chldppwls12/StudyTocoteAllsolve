from sys import stdin
input = stdin.readline

N = int(input())
l = list(map(int, input().split()))

def solution():
  memo = [i for i in l]
  for i in range(N):
    for j in range(i):
      if l[i] > l[j]:
        memo[i] = max(memo[i], memo[j] + l[i])

  return max(memo)

print(solution())