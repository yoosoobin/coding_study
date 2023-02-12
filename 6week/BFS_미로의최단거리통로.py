import sys
from collections import deque
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

dx = [-1,0,1,0]
dy = [0,1,0,-1]

a = [list(map(int,input().split())) for _ in range(7)] #문제에서 주어진 벽과 도로 표시
ch = [[0]*7 for _ in range(7)]

q = deque()
q.append((0,0)) #(1,1) 에서 출발하는것을 의미 
ch[0][0] = 1
L=0
while True:
    size = len(q)
    if size==0:
        print(-1)
        break
    for _ in range(size):
        tmp = q.popleft()
        if tmp==(6,6):
            print(L)
            sys.exit(0)
        else:
            for i in range(4):
                x=tmp[0]+dx[i]
                y=tmp[1]+dy[i]
                if 0<=x<7 and 0<=y<7:
                    if ch[x][y]==0 and a[x][y]==0:
                        ch[x][y]=1
                        q.append((x,y))
    L+=1



