# 연결 요소 개수 세기
import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[x][y] = True
    directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if position[nx][ny] and not visited[nx][ny]:
            dfs(nx,ny) # 재귀

T = int(input())
for _ in range(T):
    M,N,K = map(int, input().split())
    position = [[0] * M for _ in range(N)] # 좌표 만들기
    visited = [[False] * M for _ in range(N)] # 초기값 세팅
    for _ in range(K):
        y,x = map(int, input().split())
        position[x][y] = 1
    result = 0
    for i in range(N):
        for j in range(M):
            if position[i][j] and not visited[i][j]:
                dfs(i,j)
                result+=1
    print(result)