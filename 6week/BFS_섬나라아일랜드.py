import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(x,y):
    for h in range(8):
        xx=x+dx[h]
        yy=y+dy[h]
        if 0<=xx<n and 0<=yy<n and arr[xx][yy]==1:
            arr[xx][yy]=0
            DFS(xx,yy)

if __name__ =="__main__":
    n=int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dx = [-1,0,1,0,-1,1,-1,1]
    dy = [0,1,0,-1,-1,-1,1,1]
    cnt=0

    for a,i in enumerate(arr):
        for b,j in enumerate(i):
            if j==1:
                arr[a][b]='0'
                DFS(a,b)
                cnt+=1
                # print('cnt',cnt)
    print(cnt)

                

    






