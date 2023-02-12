import sys
from collections import deque
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')


def DFS(s,L): # 피자집을 구하는 조합구하기
    if L==m:
        tmp=[]
        for g in res:
            tmp.append(g)
        pi_com.append(tmp)

    elif s>len(pizza):
        return
    else:
        for h in range(s,len(pizza)):
            res[L]=h
            DFS(h+1,L+1)

def CAL_DIS(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)


if __name__=='__main__':
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    pizza = []
    home=[]

    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                home.append((i,j))
            elif arr[i][j]==2:
                pizza.append((i,j))
    res=[0]*m
    pi_com = []
    DFS(0,0)

    ans=[]
    for case in pi_com:
        c_tot = 0 #해당 케이스에 대한 도시의 피자 배달 거리 
        for hs in home:
            h_tot = 2147000000 # 해당 케이스에 해당 집의 피자 배달 거리 
            for pz in case:
                x1=pizza[pz][0]
                y1=pizza[pz][1]
                x2=hs[0]
                y2=hs[1]
                dis = CAL_DIS(x1,y1,x2,y2)
                if dis <h_tot:
                    h_tot=dis
            c_tot+=h_tot # 한 집의 최소배달거리를 더해준다.
        ans.append(c_tot)
    print(min(ans))    
                # sys.exit(0)
                



    

  
    


                

    






