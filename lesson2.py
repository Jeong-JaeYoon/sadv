import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split())

ans = ''
num = 1

for i in range(n):
    for j in range(m):
        if j == 0:
            ans += '{}'.format(num)
        else:
            ans += ' {}'.format(num)
        num += 1
    print(ans)
    ans = ''

## 답안

# 1
#n, m = map(int, input().split())

num = 1
for i in range(n):
    for j in range(m):
        print(num, end=' ')
        num += 1
    print()

# 2
for i in range(n):
    for j in range(m):
        print(i*m+j+1, end=' ')
    print()

# 3
for i in range(n):
    print(*range(i*m, (i+1)*m+1))

# 4
for i in range(1, n*m, m):
    print(*range(i, i+m))