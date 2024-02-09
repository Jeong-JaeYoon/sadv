import sys

sys.stdin = open('input.txt')
n, m = map(int, input().split())

if n > 100 or (m > 3 or m < 1):
    print("INPUT ERROR!")
    exit()

if m == 1:
    for i in range(n):
        print('*'*(i+1))

elif m == 2:
    for i in range(n,0, -1):
        print("*"*i)

elif m == 3:
    for i in range(n-1, -1, -1):
        print(' '*(i) + '*'*(n-i) + '*'*(n-i-1))
