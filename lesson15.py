import sys
sys.stdin = open('input.txt')

n = int(input())
A = [[0]*n for _ in range(n)]
r, c = 0, n//2
num = 0
for _ in range(n*n):
    num += 1
    A[r][c] = num
    if num%n:
        r -= 1
        c -= 1
        if r < 0:
            r = n-1
        if c < 0:
            c = n-1
    else:
        r += 1

for a in A:
    print(*a)