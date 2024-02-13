import sys
sys.stdin = open('input.txt')

n = int(input())
A = [[0] * n for _ in range(n)]

def version1():
    r, c = 0, -1
    m = n
    num = 0
    while 1:
        for i in range(m):
            num += 1
            c += 1
            A[r][c] = num
            if num == n*n: return

        m -= 1
        for i in range(m):
            num += 1
            r += 1
            A[r][c] = num
            if num == n * n: return

        for i in range(m):
            num += 1
            c -= 1
            A[r][c] = num
            if num == n * n: return

        m -= 1
        for i in range(m):
            num += 1
            r -= 1
            A[r][c] = num
            if num == n * n: return

###
version1()
for a in A:
    print(*a)