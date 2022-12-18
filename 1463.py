import sys

N = int(sys.stdin.readline())
seq = [0 for _ in range(N+1)] # 메모이제이션

for i in range(2, N+1):
    seq[i] = seq[i-1] + 1 # seq[2] = 1
    if i % 3 == 0:
        seq[i] = min(seq[i], seq[i//3] + 1) # 1 빼고 시작한 것과 비교
    if i % 2 == 0:
        seq[i] = min(seq[i], seq[i//2] + 1)
print(seq[N])
    
