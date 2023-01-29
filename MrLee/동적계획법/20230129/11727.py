import sys

N = int(sys.stdin.readline())
cnt = [0 for _ in range(N)] # Memoization

for c in range(N):
    if c == 0:
        cnt[0] = 1 # Hard Coding
    elif c == 1: 
        cnt[1] = 3 # Hard Coding
    if c > 1:
        cnt[c] = cnt[c-1] + 2* cnt[c-2] # DP
print(cnt[-1]%10007)