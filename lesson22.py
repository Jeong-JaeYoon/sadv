import sys
sys.stdin = open('input.txt')

D, K = map(int, input().split())
A = [0, 1, 0]
B = [0, 0, 1]

for i in range(3, D+1):
    A.append(A[i-2]+A[i-1])
    B.append(B[i-2]+B[i-1])

c_a, c_b = A[-1], B[-1]

a = 1
while True:
    val = K-c_a*a
    if val%c_b == 0:
        b = val // c_b
        break
    a += 1

print(a,b)

