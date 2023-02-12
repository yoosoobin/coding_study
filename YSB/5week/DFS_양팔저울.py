import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L,w):
    global pos_num
    if L ==n+1:
        if 0<w<=tot: # 양팔저울의 경우의 수는 양수 음수 대칭구조이기 때문에 양수의 경우만 보기
            pos_num.add(w) 
            
    else:
        DFS(L+1,w+wgt[L]) #무게를 더하기
        DFS(L+1,w-wgt[L]) #무게를 빼기
        DFS(L+1,w) #추를 사용하지 않음 
        

if __name__ == '__main__':
    n = int(input())
    wgt = list(map(int,input().split()))
    tot = sum(wgt)
    pos_num = set() #중복제거를 위해 set으로 받기 
    wgt.insert(0,0)
    DFS(1,0)    
    print(tot-len(pos_num))
        