from sys import stdin
input = stdin.readline

t = int(input())

def solution():
  for i in range(t):
    n = int(input())
    cl = list(map(int, input().split()))
    v = int(input())

    memo = [0] * (v+1)
    memo[0] = 1

    for i in cl:
      for j in range(1, v+1):
        if j-i >= 0:
          memo[j] += memo[j-i]

    print(memo[v])

solution()