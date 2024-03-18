import sys
sys.stdin = open('input.txt')

A = [[0]*101 for _ in range(101)]

for _ in range(int(input())):
    sx, sy = map(int, input().split())
    for x in range(sx, sx+10):
        A[x][sy:sy+10] = [1]*10

res = 0
for i in range(1, 100):
    for j in range(1, 100):
        if A[i][j]:
            for dx, dy in zip([-1, 0, 1, 0],[0, 1, 0, -1]):
                if A[i+dx][j+dy] == 0:
                    res += 1

print(res)