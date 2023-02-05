import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L,sum):
    global ans
    if L>ans:
        return 
    if sum > m:
        return
    if sum==m:
        if L<ans:
            ans = L
    else:
        for i in a:
            DFS(L+1, sum+i)


if __name__ =='__main__':
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    m = int(input())
    ans = 2147000000
    DFS(0,0)
    print(ans)




