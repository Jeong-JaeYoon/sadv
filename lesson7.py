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

## 해설

n, m = map(int, input().split())

if 1<=n<=100 and 1<=m<=3:
    if type==1:
        for i in range(1, n+1):
            print("*"*i)

    elif type==2:
        for i in range(n, 0, -1):
            print("*"*i)

    else:
        for i in range(n):
            print(' '*(n-i-1) + '*'*(2*i+1))

else:
    print('INPUT ERROR!')
