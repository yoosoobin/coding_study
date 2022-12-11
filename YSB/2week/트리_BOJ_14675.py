# 14675_단절점과 단절선

import sys
n = int(input())
tree = [[] for _ in range(n+1)]
print(tree)
for _ in range(n-1):
    a,b = map(int,input().split())
    # a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)

q = int(input())
for _ in range(q):
    t,k = map(int,input().split())
    if t == 1:
        if (len(tree[k]) < 2):
            print("no")
        else:
            print("yes")

    elif t == 2:
        print("yes")