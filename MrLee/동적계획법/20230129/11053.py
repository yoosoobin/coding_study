import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
DP = [1] * N # 자기 자신
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            DP[i] = max(DP[i], DP[j] + 1) # DP

print(max(DP))