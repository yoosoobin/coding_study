import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
heap = []
for i in range(N):
    a = int(input())
    if a == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    heapq.heappush(heap, -a)