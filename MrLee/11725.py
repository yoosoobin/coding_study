import sys
sys.setrecursionlimit(10**6)
def dfs(start, tree, parent):
    for i in tree[start]: # tree[1] : [6,4] -> tree[6] : [1,3] -> tree[1] : [6,4]
        if parent[i] == 0: # parent[6] : 0 -> parent[1] : 0 -> parent[1] : 6 Pass, 4
            parent[i] = start # parent[6] : 부모 1 -> parent[1] : 부모 6 -> parent[4] : 부모 1
            dfs(i, tree, parent) # dfs(6, tree, parent) -> dfs(1,tree,parent) -> dfs(4, tree, parent)

N = int(sys.stdin.readline())

tree_list = [[] for _ in range(N+1)] # 트리 구조
parent_list = [0 for _ in range(N+1)] # 전부 0으로 초기화

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree_list[a].append(b) # 트리 구조
    tree_list[b].append(a) # 트리 구조

dfs(1,tree_list, parent_list) # 시작 노드 : 1

for i in range(2, N+1):
    print(parent_list[i])