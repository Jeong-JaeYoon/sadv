import sys
sys.stdin = open('input.txt')

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

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

def version1_2():
    r, c = 0, -1
    m = n
    num = 0
    while 1:
        for idx, (dr, dc) in enumerate(zip(dR, dC)):
            for i in range(m):
                num += 1
                r += dr
                c += dc
                A[r][c] = num
                if num == n*n:return
            if idx%2 == 0:
                m -= 1

def version2():
    r, c = 0, 0
    m = n - 1
    num = 0
    while 1:
        for dr, dc in zip(dR, dC):
            for i in range(m):
                num += 1
                A[r][c] = num
                if num == n*n: return
                r, c = r+dr, c+dc
        r, c, m = r+1, c+1, m-2


def version3():
    r, c = 0, -1
    num = 0
    while 1:
        for dr, dc in zip(dR, dC):
            while 1:
                nr, nc = r + dr, c + dc
                if nr<0 or nr>=n or nc<0 or nc>=n:
                    break
                if A[nr][nc]:
                    break
                r, c = nr, nc
                num += 1
                A[r][c] = num
                if num == n*n: return
#
# version1()
# version1_2()
# version2()
# version3()
#
# for a in A:
#     print(*a)

B = [[1]*(n+2)] + \
    [[1]+[0]*n+[1] for _ in range(n)] + \
    [[1]*(n+2)]
def version4():
    r, c = 1, 0
    num = 0
    while 1:
        for dr, dc in zip(dR, dC):
            while 1:
                if B[r+dr][c+dc]:
                    break
                r, c = r+dr, c+dc
                num += 1
                B[r][c] = num
                if num == n*n: return

version4()
for b in B[1:n+1]:
    print(*b[1:n+1])