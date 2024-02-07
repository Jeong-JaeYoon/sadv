import sys

sys.stdin = open('input.txt')

n = int(input())
li = [['']*n for _ in range(n)]

num = 0
for i in range(n):
    for j in range(n):
        if i%2 == 0:
            li[j][i] = chr(num+65)
        else:
            li[-j-1][i] = chr(num+65)
        num = (num+1)%26

for a in li:
    print(*a)

## 해설
n = int(input())
A = [['']*n for _ in range(n)]

num = 0
for c in range(n):
    for k in range(n):
        if c%2:
            r = n-k-1
        else:
            r = k
        A[r][c] = chr(num+65)
        num = (num+1)%26

for a in A:
    print(*a)
