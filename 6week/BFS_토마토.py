import sys
from collections import deque
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

m,n = map(int,input().split()) #행,열 정보 받기
arr=[list(map(int,input().split())) for _ in range(n)]

case1 = 0 #모두 익어있다
for e in arr:
    if 0 not in e:
        case1 +=1
if case1 == n:
    print(0)
    sys.exit(0)

dx=[-1,0,1,0]
dy=[0,1,0,-1]
ans = []
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            ans.append((i,j))
q=deque()
for h in ans:
    q.append(h)

cnt = 0    
while q:
    size= len(q)
    for _ in range(size):
        tmp = q.popleft()
        for j in range(4):
            xx=tmp[0]+dx[j]
            yy=tmp[1]+dy[j]
            if 0<=xx<n and 0<=yy<m and arr[xx][yy]==0:
                arr[xx][yy]=1
                q.append((xx,yy))
    cnt+=1
    check=0
    for w in arr:
        if 0 not in w:
            check+=1
    if check ==n:
        print(cnt)
        sys.exit(0)
            
print(-1)



















            # print('**',i,j)
            # cnt = 0
            # q =deque()
            # q.append((i,j))
            # while q:
            #     size = len(q)
            #     for _ in range(size):
            #         tmp = q.popleft()
            #         print('tmp',tmp)
            #         for h in range(4):
            #             xx=tmp[0]+dx[h]
            #             yy=tmp[1]+dy[h]
            #             if 0<=xx<=m-1 and 0<=yy<=n-1 and arr[xx][yy]==0:
            #                 arr[xx][yy]=1
            #                 q.append((xx,yy))
            #                 print('append',xx,yy)
            #     cnt+=1
            #     print('***cnt+1***')
            # if cnt>ans:
            #     ans = cnt
            #     print('!!!!!!!!!!!!!!!!tmp_ans',ans)
                    









       
  
    


                

    






