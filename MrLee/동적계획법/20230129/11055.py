import sys

input = sys.stdin.readline
N = int(input())
li = list(map(int, input().split()))

DP = [x for x in li] # Memoization

for i in range(N):
    for j in range(i):
        if li[i] > li[j]:
            DP[i] = max(DP[i], DP[j] + li[i]) # DP
print(max(DP))