import sys
sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(v):
    if v==n+1: #종료지점임
        for i in range(1,n+1):
            if ch[i]==1:
                print(i,end=' ')
        print()

    else:
        ch[v]=1 #부분집합에 사용
        DFS(v+1)
        ch[v]=0 #부분집합에 미사용
        DFS(v+1)
        


if __name__ == '__main__':
    n=int(input())
    ch = [0]*(n+1)
    DFS(1)


