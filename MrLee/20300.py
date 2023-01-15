import sys

N = int(sys.stdin.readline())
PT_list = list(map(int, input().split()))
if len(PT_list) % 2 != 0:
    PT_list.append(0)
PT_list_asc = sorted(PT_list)
PT_list_des = sorted(PT_list, reverse=True)
print(max([PT_list_des[i] + PT_list_asc[i] for i in range(N)]))