import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L,tsum,ssum,s,remain):
    global ans
    if tsum>m:
        return
    if ssum + remain <ans:
        return
    if L == n:
        if tsum<=m and ssum>ans:
            # print(score_list)
            # print(sum(score_list))
            ans = ssum

    else:
        for j in range(s,n+1):
            if ch[j] == 0:
                ch[j]=1
                # score_list.append(scr[j])
                DFS(L+1,tsum+time[j],ssum+scr[j],s+1,sum(scr[j+1:]))
                ch[j]=0
                # score_list.pop()
                DFS(L+1,tsum,ssum,s+1,sum(scr[j+1:]))


if __name__ == '__main__':
    n,m = map(int,input().split())
    scr = [0]*(n+1)
    time = [0]*(n+1)
    ch = [0]*(n+1)
    for i in range(1,n+1):
        s,t = map(int,input().split())
        scr[i] = s
        time[i] = t
    ans = 0
    score_list = []
    DFS(0,0,0,1,0)
    print(ans)
    
        