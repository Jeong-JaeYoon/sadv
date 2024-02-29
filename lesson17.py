import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())

A = []

for _ in range(h):
    a = list(input())
    A.append(a)

c = int(input())

if c == 0:
    B = [['']*h for _ in range(w)]

    for i in range(h):
        for j in range(w):
            B[j][i] = A[h-1-i][j]

    print(h, w)
    for b in B:
        print(''.join(b))

if c == 1:
    B = [[''] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            B[i][j] = A[h-1-i][w-1-j]

    print(w, h)
    for b in B:
        print(''.join(b))

if c == 2:
    B = [[''] * h for _ in range(w)]

    for i in range(h):
        for j in range(w):
            B[j][i] = A[i][w-1-j]

    print(h, w)
    for b in B:
        print(''.join(b))

if c == 3:
    print(w, h)
    for a in A[::-1]:
        print(''.join(a))

if c == 4:
    A = [a[::-1] for a in A]
    print(w, h)
    for a in A:
        print(''.join(a))

import copy
import sys
sys.stdin = open('input.txt')

W, H = map(int, input().split())
A = [list(input().strip()) for _ in range(H)]

c = int(input())
if c == 0 or c == 2:
    B = [[''] * H for _ in range(W)]
else:
    B = copy.deepcopy(A)


if c == 0:
    for i in range(H):
        for j in range(W):
            B[j][H-1-i] == A[i][j]
    H, W = W, H

if c == 1:
    for i in range(H):
        for j in range(W):
            B[H-1-i][W-1-j] == A[i][j]

if c == 2:
    for i in range(H):
        for j in range(W):
            B[W-1-j][i] == A[i][j]
    H, W = W, H

if c == 3:
    B.reverse()

if c == 4:
    B = [b[::-1] for b in B]

print(W, H)
for b in B:
    print(''.join(b))


