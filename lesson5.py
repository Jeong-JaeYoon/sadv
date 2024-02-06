## 해설

import sys
sys.stdin = open('input.txt')

n = int(input())
A = [['']*n for _ in range(n)]

# ascii A=65, a=97
print(ord('A'), ord('a'))
print(chr(65), chr(97))

num = 0
for c in range(n-1, -1, -1):
    for r in range(n-1, -1, -1):
        A[r][c] = chr(num+65)
        num = (num+1)%26

for a in A:
    print(*a)