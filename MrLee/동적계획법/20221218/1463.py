N = int(input())
cnt = [0 for _ in range(N)]

for c in range(N):
    if c == 0:
        cnt[0] = 1
    elif c == 1:
        cnt[1] = 2
    if c > 1:
        cnt[c] = cnt[c-1] + cnt[c-2] 
print(cnt[-1]%10007)
