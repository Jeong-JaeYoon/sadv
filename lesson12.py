import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

A = [[0]*(i+1) for i in range(n)]

for a in A:
    a[0] = a[-1] = 1

for idx, a in enumerate(A):
    if idx > 1:
        for i in range(1, len(a)-1):
            a[i] = A[idx-1][i-1] + A[idx-1][i]

if m == 1:
    for a in A:
        print(*a)

elif m == 2:
    for i, a in enumerate(A[::-1]):
        print(' '*i, end='')
        print(*a)

else:
    for i in range(n):
        for j in range(i+1):
            r, c = n-j-1, n-i-1
            print(A[r][c], end=' ')
        print()


## 해설
n, m = map(int, input().split())
A = [[1]*i for i in range(1, n+1)]
for i in range(2, n):
    for j in range(1, i):
        A[i][j] = A[i-1][j-1]+A[i-1][j]

if m == 1:
    for a in A:
        print(*a)

if m == 2:
    for i, a in enumerate(A[::-1]):
        print(' '*i, end='')
        print(*a)

if m == 3:
    for i in range(n):
        for j in range(i+1):
            r, c = n-j-1, n-i-1
            print(A[r][c], end = ' ')
        print()