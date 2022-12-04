from collections import deque

N, K = list(map(int, input().split()))
dq = deque()
for n in range(1,N+1):
    dq.append(n)
result = []
while True:
    
    dq.rotate(-K+1)
    if len(dq) == 0:
        break
    else:
        result.append(dq.popleft())

result = str(result)
print(f"<{result[1:-1]}>")