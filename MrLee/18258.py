from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque()

for n in range(N):
    inp = sys.stdin.readline().split()
    if inp[0] == "push":
        dq.append(int(inp[1]))
    if inp[0] == "pop":
        if len(dq) != 0:
            result = dq.popleft()
            print(result)
        else:
            print(-1)
        
    
    if inp[0] == "size":
        print(len(dq))
        
    if inp[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    if inp[0] == "front":
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    if inp[0] == "back":
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)
        
