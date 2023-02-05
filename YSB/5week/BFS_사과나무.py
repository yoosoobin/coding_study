import sys
from collections import deque
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

n = int(input())
trees = [deque(map(int,input().split())) for _ in range(n)]
trees.insert(0,0)
mid = n//2+1
tot = 0
for i in range(1,n+1):
    if i==mid:
        tot+=sum(trees[i])
    elif i<mid:
        a = mid-i
        for _ in range(a):
            trees[i].popleft()
            trees[i].pop()
        tot+=sum(trees[i])
    else:
        a=i-mid
        for _ in range(a):
            trees[i].popleft()
            trees[i].pop()
        tot+=sum(trees[i])
print(tot)



