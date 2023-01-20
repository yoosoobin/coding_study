#1m, 2m의 길이를 갖는 선으로 네트워크를 자르려고 한다.
# 네트워크 선의 길이가 Nm이라면 몇 가지의 자르는 방법을 생각할 수 있는가?
import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
dy=[0]*(n+1)
dy[1]=1
dy[2]=2
for i in range(3, n+1):
    dy[i]=dy[i-1]+dy[i-2]

print(dy[n])

    
