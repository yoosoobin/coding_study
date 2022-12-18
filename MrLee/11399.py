import sys

N = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

temp = 0
for i in range(1,N+1):
    temp += i*lst[N-i]
print(temp)