import sys
sys.stdin = open('input.txt')

# 채우고 이동
# (0,n-1)에서 시작

n = int(input())
A = [[' ']*(2*n-1) for _ in range(2*n-1)]
r, c = 0, n-1
m = n-1
num = 0

while 1:
    for dr, dc in zip([1, 1, -1, -1], [-1, 1, 1, -1]):
        for i in range(m):
            A[r][c] = chr(num + 65)
            num = (num+1) % 26
            r += dr
            c += dc
    r += 1
    m -= 1
    if m == 0:
        A[r][c] = chr(num + 65)
        break

for a in A:
    print(*a)
