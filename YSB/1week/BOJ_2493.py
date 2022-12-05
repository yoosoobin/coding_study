# https://www.acmicpc.net/problem/2493
import sys
r = sys.stdin.readline

# 입력 받기
n = int(input())
t_list = list(map(int,input().split()))
answer = []
stk = []
for i in range(n): # 탑의 수만큼 반복
    h = t_list[i]  # 현재 탑의 높이 h
    print('h',h)  
    if stk:
        print(stk)
        while stk:
            if stk[-1][0] < h :  #현재 탑의 높이가 이전탑보다 크다면 이전 탑 pop
                stk.pop()
                if not stk:  # 이전탑이 없다면 0 print
                    print(0, end=' ')
            elif stk[-1][0] > h: # 현재 탑의 높이가 이전탑보다 작다면 이전 탑의 인덱스+1 print
                print(stk[-1][1]+1, end=' ')
                break
            else : 
                print(stk[-1][1]+1, end=' ')  #현재 탑의 높이가 이전 탑과 같다면 이전탑의 인덱스+1 print
                stk.pop()
                break
        stk.append([h, i]) # 현재 탑의 높이와 인덱스 append
    else:
        print(0, end=' ')
        stk.append([h,i])