import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L,s):
    global cnt
    global m
    global k
    if L == k:
        if sum(res)%m ==0:
            cnt+=1
    else:
        for i in range(s,n):
            res[L] = a[i]
            DFS(L+1, i+1)

if __name__ =='__main__':
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())
    cnt = 0
    res = [0]*k
    DFS(0,0)
    print(cnt)