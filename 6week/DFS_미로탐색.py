import sys

# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
        # print('path',path)
        return
    else:
        for i in range(4):
            if 0<=x+dx[i]<=6 and 0<=y+dy[i]<=6 and a[x+dx[i]][y+dy[i]]==0:
                # path.append((x+dx[i],y+dy[i]))
                a[x+dx[i]][y+dy[i]]=1
                # print(x+dx[i],y+dy[i])
                DFS(x+dx[i],y+dy[i])
                # path.pop()
                a[x+dx[i]][y+dy[i]]=0

if __name__ == "__main__":
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    a = [list(map(int,input().split())) for _ in range(7)] #문제에서 주어진 벽과 도로 표시
    cnt = 0
    path=[]
    a[0][0]=1
    DFS(0,0)
    print(cnt)






