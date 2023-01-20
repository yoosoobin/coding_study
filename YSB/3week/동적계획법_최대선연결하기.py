# 왼쪽의 번호와 오른족의 번호 끼리 선으로 연결하려고 한다.
# 왼쪽번호는 무조건 위에서부터 차례로 1부터 N까지 오름차순 나열되어 있다.
# 오른쪽 번호 정보가 위부터 아래 순서로 주어짐 서로 선이 겹치지 않고 최대 몇개 선으로 연결가능?

import sys
sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)

dy=[0]*(n+1)
dy[1]= arr[1]

res=0

for i in range(2,n+1):
    max = 0 
    for j in range(i-1,0,-1):
        if arr[j]<arr[i] and dy[j] >max:  # i가 증가수열의 마지막 항이
            max = dy[j]

    dy[i] = max+1

    if dy[i] >res:
        res = dy[i]

print(res)
