import sys

sys.stdin = open('input.txt')
n = int(input())

if (1 <= n <= 100) and (n%2 == 1):

    h = n//2

    for i in range(h+1):
        print(' '*i + '*'*(2*i+1))

    for j in range(h, 0, -1):
        print(' '*(j-1) + '*'*(2*j-1))
else:
    print('INPUT ERROR!')