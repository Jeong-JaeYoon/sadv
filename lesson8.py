import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

if ((1 <= n <= 100) and (n % 2 == 1)) and (1 <= m <= 4):
    h = n//2 + 1

    if m == 1:
        for i in range(1, h+1):
            print("*" * i)
        for j in range(n-h, 0, -1):
            print("*" * j)

    elif m == 2:
        for i in range(h-1, -1, -1):
            print(" "*i + '*'*(h-i))
        for j in range(1, h):
            print(' '*j + '*'*(h-j))

    elif m == 3:
        for i in range(h):
            print(' '*i + '*'*(n-(2*i)) + ' '*i)
        for j in range(h-2, -1, -1):
            print(' '*j + '*'*(n-(2*j)) + ' '*j)

    else:
        for i in range(h):
            print()


else:
    print("INPUT ERROR!")