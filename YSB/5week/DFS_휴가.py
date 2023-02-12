import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L,t,p):
    global ans
    if t>n or L>n:
        return
    if L == n:
        if p>ans:
            ans = p
    else:
        DFS(L+time[L], t+time[L],p+pay[L])
        DFS(L+1,t,p)

if __name__ == '__main__':
    n = int(input())
    time = []
    pay = []
    for _ in range(n):
        t,p = map(int,input().split())
        time.append(t)
        pay.append(p)
    ans = -2147000000
    DFS(0,0,0)
    print(ans)




    
        