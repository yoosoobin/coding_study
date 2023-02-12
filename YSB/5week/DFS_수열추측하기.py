import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L):
    if L == n:
        tmp = [x*y for x,y in zip(res, con)]
        if sum(tmp) == f:
            for j in res:
                print(j,end=' ')
            sys.exit(0)
    else:
        for i in range(1,n+1):
            if ck[i]==0:
                ck[i]=1
                res[L]=i
                DFS(L+1)
                ck[i]=0        

if __name__ == '__main__':
    n,f = map(int,input().split())
    res = [0]*n
    con = [1]*n
    ck = [0]*(n+1)
    for i in range(1,n):
        con[i] = con[i-1]*(n-i)//i
    DFS(0)