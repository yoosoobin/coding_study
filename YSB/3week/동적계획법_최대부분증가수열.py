#N개의 자연수로 이루어진 수열이 주어졌을 때, 그 중에서 가장 길게
#증가하는 원소들의 집합을 찾는 프로그램을 작성하라 

import sys

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)

dy = [0]*(n+1)
dy[1]=1

res = 0

for i in range(2, n+1):
    max = 0
    for j in range(i-1,0,-1):
        if arr[j]<arr[i] and dy[j] > max:
            max = dy[j]

    dy[i] = max + 1

    if dy[i] > res:
        res = dy[i]

print(res)