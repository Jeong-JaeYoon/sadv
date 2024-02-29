import sys
sys.stdin = open('input.txt')

n = int(input())
A = []

for _ in range(n):
    a = list(map(int, input().split()))
    A.append(a)

def rotation(inp):

    B = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            B[r][c] = inp[n-1-c][r]

    return B

turn = {'90':1, '180':2, '270':3, '360':0}

while True:
    inp = int(input())
    if inp == 0:
        break
    a = turn[str(inp)]
    for _ in range(a):
        A = rotation(A)

for a in A:
    print(*a)