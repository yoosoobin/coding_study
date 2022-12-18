import sys

N = int(sys.stdin.readline())
energy_list = list(map(int, input().split()))
energy_list = sorted(energy_list, reverse=True)

energy_max = energy_list.pop(0)
print(energy_max + sum(energy_list)/2)