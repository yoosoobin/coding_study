import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L):
    global cnt
    if L == m:
        cnt +=1
        for j in res:
            print(j, end = ' ')
        print()
    else:
        for i in range(1, n+1):
            if ck[i] == 0:
                ck[i] = 1
                res[L] = i
                DFS(L+1)
                ck[i] = 0
                
if __name__ == '__main__':
    n,m = map(int,input().split())
    cnt = 0
    res = [0]*m
    ck = [0]*(n+1)
    DFS(0)
    print(cnt)

