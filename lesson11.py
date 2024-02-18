import sys
sys.stdin = open('input.txt')

n = int(input())

A = [[0]*(i+1) for i in range(n)]

dR = [1, 0, -1]
dC = [1, -1, 0]
r, c = -1, -1
m = n
num = 0

while m > 0:
    for dr, dc in zip(dR, dC):
        for _ in range(m):
            r += dr
            c += dc
            A[r][c] = num%10
            num += 1
        m -= 1

for a in A:
    print(*a)

## 해설

n = int(input())
A = [[0]*i for i in range(1, n+1)]

def make_A():
    r = c = -1
    m = n
    num = 0

    while 1:
        for dr, dc in zip([1,0,-1], [1,-1,0]):
            for i in range(m):
                r,c = r+dr, c+dc
                A[r][c] = num
                num = (num+1)%10
            m -= 1
            if m == 0:
                return

make_A()

for a in A:
    print(*a)
