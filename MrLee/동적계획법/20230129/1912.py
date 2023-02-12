import sys

input = sys.stdin.readline
N = int(input())
DP = list( map(int, input().split(' ')))
 
for i in range(1, N):
    DP[i] = max(DP[i], DP[i] + DP[i-1]) # DP
    
print(max(DP))