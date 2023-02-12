import sys
from collections import deque
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n=int(input())
arr =[list(map(int,input().split())) for _ in range(n)]
mn = 2147000000
mx = -2147000000
ans=-2147000000

for i in arr:
    for j in i:
        if j<mn:
            mn=j
        if j>mx:
            mx=j

for rain in range(mn,mx):
    # print('rain',rain)
    cnt=0
    ch = [[0]*n for _ in range(n)]
    for a,x in enumerate(arr): # 물에 잠기고 안잠기고 체크
        for b,y in enumerate(x):
            if y<=rain:
                ch[a][b]=0 
            else:
                ch[a][b]=1
    for c in range(n):
        for d in range(n):
            if ch[c][d]==1:
                q=deque()
                q.append((c,d))
                # print('c',c,'d',d)
                ch[c][d]=0
                while q:
                    size = len(q)
                    for _ in range(size):
                        tmp = q.popleft()
                        for e in range(4):
                            xx = tmp[0] + dx[e]
                            yy = tmp[1] + dy[e]
                            # print('xx','yy',xx,yy)
                            if 0<=xx<n and 0<=yy<n and ch[xx][yy] ==1:
                                ch[xx][yy]=0
                                q.append((xx,yy))
                                # print('q',q)
                cnt+=1
    if cnt>ans:
        ans=cnt
       

print(ans)            
    


                

    






