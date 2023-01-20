# https://www.acmicpc.net/problem/11047
n,k = map(int,input().split())
c_list = []
for i in range(n):
    c_list.append(int(input()))
c_list.sort(reverse=True)

cnt=0
for i in c_list:
    cnt += k//i
    k %= i
print(cnt)