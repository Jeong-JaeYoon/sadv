import sys
sys.stdin = open('input.txt')

A = [[0]*100 for _ in range(100)]

for _ in range(int(input())):
    X, Y = map(int, input().split())
    for x in range(X, X+10):
        A[x][Y:Y+10] = [1]*10

print(sum(sum(a) for a in A))
