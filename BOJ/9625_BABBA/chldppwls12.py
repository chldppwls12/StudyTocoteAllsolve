from sys import stdin
input = stdin.readline

K = int(input())

def solution():
  am = [1, 0]
  bm = [0, 1]

  for i in range(2, K+1):
    a = am[i-1] + am[i-2]
    am.append(a)

    b = bm[i-1] + bm[i-2]
    bm.append(b)

  print(am[K], bm[K])

solution()