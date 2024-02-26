import sys
sys.stdin = open('input.txt')

n = int(input())
A = [[1]*n for _ in range(n)]

def fill_A():
    r = c = 0
    num = 1
    while 1:
        if r < n-1:
            r += 1
        else:
            c += 1

        while 1:
            num += 1
            A[r][c] = num
            if num == n * n: return
            if r == 0 or c == n-1:
                break
            r -= 1
            c += 1

        if c < n-1:
            c += 1
        else:
            r += 1

        while 1:
            num += 1
            A[r][c] = num
            if num == n*n: return
            if r == n-1 or c == 0:
                break
            r += 1
            c -= 1

fill_A()

for a in A:
    print(*a)