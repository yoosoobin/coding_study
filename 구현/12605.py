import sys

input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    s = list(input().rstrip().split(' '))
    s = s[::-1]
    print("Case #" + str(i) + ":", *s)