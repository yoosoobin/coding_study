import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    inp = sys.stdin.readline().split()
    if inp[0] == "push":
        stack.append(int(inp[1]))
    if inp[0] == "pop":
        if len(stack) > 0:
            print(stack[-1])
            stack.pop(-1)
        else:
            print(-1)
    
    if inp[0] == "size":
        print(len(stack))
    if inp[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    if inp[0] == "top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)