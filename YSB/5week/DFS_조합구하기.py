import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L,s):
    global cnt
    if L == m :
        cnt +=1
        for j in res:
            print(j, end = ' ')
        print()
    else:
        for i in range(s+1, n+1):
            res[L] = i
            DFS(L+1,i)

                
                
if __name__ == '__main__':
    n,m = map(int,input().split())
    cnt = 0
    res = [0]*m
    DFS(0,0)
    print(cnt)

