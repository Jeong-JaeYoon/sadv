import copy
import sys
sys.stdin = open('input.txt')

n = int(input())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

answer = sys.maxsize

num = 0
for a, b in zip(A, B):
    num += sum(c != d for c, d in zip(a, b))

answer = min(num, answer)

# A_right
C = copy.deepcopy(B)

num = 0
for i in range(n):
    for j in range(i+1):
        C[i][j] = A[n-1-j][i-j]

for a, b in zip(B, C):
    num += sum(c != d for c, d in zip(a, b))

answer = min(num, answer)

# A_right_reverse
num = 0
for c in C:
    c.reverse()

for a, b in zip(B, C):
    num += sum(c != d for c, d in zip(a, b))

answer = min(num, answer)

# A_left
C = copy.deepcopy(B)

num = 0
for i in range(n):
    for j in range(i+1):
        C[i][j] = A[n-1-i+j][n-1-i]

for a, b in zip(B, C):
    num += sum(c != d for c, d in zip(a, b))

answer = min(num, answer)

# A_left_reverse
num = 0
for c in C:
    c.reverse()

for a, b in zip(B, C):
    num += sum(c != d for c, d in zip(a, b))

answer = min(num, answer)

# reverse
C = copy.deepcopy(A)

num = 0
for c in C:
    c.reverse()

for a, b in zip(B, C):
    num += sum(c != d for c, d in zip(a, b))

answer = min(num, answer)

num = 0
for i in range(n):
    for j in range(i+1):
        C[i][j] = A[n-1-j][i-j]

for a, b in zip(B, C):
    num += sum(c != d for c, d in zip(a, b))

answer = min(num, answer)

num = 0
for i in range(n):
    for j in range(i+1):
        C[i][j] = A[n-1-i+j][n-1-i]

for a, b in zip(B, C):
    num += sum(c != d for c, d in zip(a, b))

answer = min(num, answer)

print(answer)
