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
    for i in range(n-1, -1, -1):
        print(*A[i])

else:
    pass