import sys
sys.stdin = open('input.txt')

n = int(input())

for i in range(1, n+1):
    print(*range(i, i+n*(n-1)+1, n))

## 해설 1
n = int(input())
A = [[0]*n for _ in range(n)]

num = 1
for c in range(n):
    for r in range(n):
        A[r][c] = num
        num += 1

for a in A:
    print(*a)

## 해설 2
for i in range(1, n+1):
    print(*range(i,n*n+1,n))