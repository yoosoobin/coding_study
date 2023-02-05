import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L):
    global cnt
    if L == n:
        cnt+=1
        # print(path)

    else:
        for i in range(2,n+1):
            if arr[L][i] ==1 and ch[i]==0:
                ch[i]=1
                # path.append(i)
                DFS(i)
                ch[i]=0
                # path.pop()


if __name__ == '__main__':
    n, m = map(int,input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        c,r = map(int,input().split())
        arr[c][r] = 1
    ch = [0]*(n+1)
    cnt = 0
    ch[1] = 1
    # path=[1]
    DFS(1)
    print(cnt)
