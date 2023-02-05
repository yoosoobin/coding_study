import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')


def DFS(L,sum):
    global cnt
    if sum>n:
        return
    if L==len(cash):
        if sum==n:
            cnt+=1

    else:
        for i in range(count[L]+1):
            DFS(L+1,sum+cash[L]*i)


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    cash = []
    count = []
    for _ in range(k):
        c,t = map(int,input().split())
        cash.append(c)
        count.append(t)
    cash.insert(0,0)
    count.insert(0,0)
    cnt = 0
    DFS(1,0)
    print(cnt)


    