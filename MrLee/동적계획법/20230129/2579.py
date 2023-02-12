import sys

N = int(sys.stdin.readline())

stair = [0]*301 # 계단 수
for i in range(N):
    stair[i]=int(sys.stdin.readline()) # 숫자

DP = [0]*301 # Memoization
DP[0] = stair[0] # Hard Coding
DP[1] = stair[0]+stair[1] # Hard Coding
DP[2] = max(stair[0]+stair[2], stair[1]+stair[2]) # Hard Coding 

for i in range(3, N):
    DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2]+stair[i]) # DP

print(DP[N-1])