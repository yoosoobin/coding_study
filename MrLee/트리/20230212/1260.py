# 모든
# 인접 행렬을 이용해 풀어보기
from collections import deque

def dfs(graph,start_node):
    visited, need_visit = list(), list()
    
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node], reverse=True))
    
    return visited

def bfs(graph, start_node):
    visited, need_visit = list(), deque()
    
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node]))
    
    return visited
N,M,start_node = map(int, input().split())
graph = {}
for n in range(N):
    if graph.get(n) == None:
        graph[n] = [] # 모든 노드 추가
for _ in range(M):
    parent, child = map(int, input().split())
    if graph.get(parent) == None:
        graph[parent] = []
    graph[parent].append(child)
    if graph.get(child) == None:
        graph[child] = []
    graph[child].append(parent)   

result = dfs(graph, start_node)
for i in result:
    print(i, end = " ")
result = bfs(graph, start_node)
print("")
for i in result:
    print(i, end = " ")