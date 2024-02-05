import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split())

for i in range(1, n*m+1, m):
    if (i//m) % 2 == 0:
        print(*range(i, i+m))
    else:
        print(*reversed(range(i, i+m)))

## 해설

n, m = map(int, input().split())

for i in range(n):
    s = i*m+1
    e = s+m
    if i%2:
        print(*range(e-1, s-1, -1))
    else:
        print(*range(s,e))