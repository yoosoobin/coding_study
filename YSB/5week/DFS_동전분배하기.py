import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L,a,b,c):
    global ans
    if L == n+1:
        if (a!=b and b!=c and a!=c) and max(a,b,c) - min(a,b,c) < ans:
            ans = max(a,b,c) - min(a,b,c)
    else:
        DFS(L+1,a+coin[L],b,c)
        DFS(L+1,a,b+coin[L],c)
        DFS(L+1,a,b,c+coin[L])

if __name__ == '__main__':
    n = int(input())
    coin = [int(input()) for _ in range(n)]
    coin.insert(0,0)
    ans =2147000000
    DFS(1,0,0,0)
    print(ans)