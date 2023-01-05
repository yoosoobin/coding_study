# https://www.acmicpc.net/problem/10773
n =int(input())
sum_list = []

for i in range(n):
    s = int(input())
    if s != 0:
        sum_list.append(s)
    else:
        sum_list.pop()
print(sum(sum_list))