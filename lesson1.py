import sys
from collections import deque

# li = [1,2,3,4,5,6]
# for x in li:
#     print(x)

# shift + f10 : 설정된 파일 실행
# ctrl + shift + f10 : 현재 커서 위치에 파일 실행

li = [1,2,3]
for x in li:
    print(x)

# ctrl + / : 주석/해제
# ctrl + d : 커서행 복사
# shitf + del : 커서행 삭제
# alt + enter : 모듈 import 가능

def func(l):
    print(id(l))
    l = [3,4,5]
    print(id(l))

func(li)
print(id(li))

###########################################################
sys.stdin = open('input.txt')

## 문자열 1개 입력받아서 처리
s = input().strip()  # 양쪽 white space(공백) 제거

## 문자열 여러 개 한 줄에 공백 기준으로 입력
s = input().split() # 공백 기준 리스트로 분류, strip() 생략 가능

## 정수 한 개 입력
s = int(input())

## 정수 두 개 입력
s = input().split()
s = list(map(int,s))

s = list(map(int, input().split()))
# map(func, s)     # s의 각 원소 x에 대해 func(x) 값으로 변환
#                  # iterator 반환

## 3개의 줄마다 한 개 문자열 입력
li = []
for i in range(3):
    li.append(input().strip())
print(li)

li = [input().strip() for _ in range(3)]

## 3개의 줄마다 정수 입력
li = [int(input()) for _ in range(3)]
print(li)

## 3개의 줄마다 문자열 5개 입력 : 3*5 2d list
li = [input().split() for _ in range(3)]

## 3개의 줄마다 정수 5개 입력
li = [list(map(int, input().split())) for _ in range(3)]

## print(), *: unpacking
li = [1,2,3,4,5]
print(li)
print(*li)
print(*li, sep = ' ', end = '\n')
print(*li, sep = '')
print(*li, sep = '\n')

## f-string
print(f'li = {li}')
print('li = {}'.format(li))