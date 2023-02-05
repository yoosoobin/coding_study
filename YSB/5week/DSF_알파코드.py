import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

def DFS(L,s):
    global cnt
    if L==len(n):
        print(s)
        cnt+=1
    else:
        for i in range(1,3):
            if i ==1 :
                if int(n[L])==0:
                    break
                else:
                    # print(L+1,s+chr(int(n[L])+64))
                    DFS(L+1,s+chr(int(n[L])+64))
            else:
                if L<len(n)-1 and int(n[L]+n[L+1])<27:
                    # print(L+2,s+chr(int(n[L]+n[L+1])+64))
                    DFS(L+2,s+chr(int(n[L]+n[L+1])+64))
            

if __name__ == "__main__":
    n = list(input())
    n.insert(0,0)
    cnt = 0
    DFS(1,s='')
    print(cnt)


