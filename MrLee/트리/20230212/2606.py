from collections import deque
N = int(input())
L = int(input())
graph = {}
for n in range(1,N+1):
    graph[n] = []
for _ in range(L):
    link = list(map(int, input().split()))
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])
def bfs():
    q = deque([1])
    visited = list()
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])
    visited.pop(0)
    return len(visited)
print(bfs())