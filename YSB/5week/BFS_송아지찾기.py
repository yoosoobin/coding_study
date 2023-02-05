import sys
from collections import deque
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

max = 10000
n,m = map(int,input().split())
ch = [0]*(max+1)
dis = [0]*(max+1)
dis[n]=0
ch[n]=1
deq = deque()
deq.append(n)

while deq:
    now = deq.popleft()
    if now ==m :
        break
    for next in (now-1, now+1, now+5):
        if 1<=next<=max:
            if ch[next]==0:
                deq.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])

