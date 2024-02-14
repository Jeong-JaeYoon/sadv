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
