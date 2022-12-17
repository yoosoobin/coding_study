from collections import deque

N = int(input())

dq = deque()
for n in range(1,N+1):
    dq.append(n)
while True:
    if len(dq) == 1:
        result = dq.pop()
        break
    else:
        dq.popleft()
        change = dq.popleft()
        dq.append(change)
print(result)
    