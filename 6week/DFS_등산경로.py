import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(x,y):
    global cnt
    if (x,y)== fp:
        cnt+=1
        return
    else:
        for h in range(4):
            xx=x+dx[h]
            yy=y+dy[h]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and ch[xx][yy]==0 and arr[x][y]<arr[xx][yy]:
                ch[xx][yy]=1
                DFS(xx,yy)
                ch[xx][yy]=0


if __name__=='__main__':
    n=int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    s=2147000000
    f=-2147000000
    for a,i in enumerate(arr):
        for b,j in enumerate(i):
            if j<s:
                s = j
                sp=(a,b) #시작점
            if j>f:
                f=j
                fp=(a,b) #도착점
    cnt =0
    ch[sp[0]][sp[1]]=1
    DFS(sp[0],sp[1])
    print(cnt)






