from collections import deque
## N : start_point, K : end_point 
N, K = map(int, input().split())
time = [0 for _ in range(100001)]
# N, K가 주어졌을 때 최단 시간
# -1로 걷기
# +1로 걷기
# *2로 순간이동
def bfs():
    q = deque([N])
    while q:
        current_point = q.popleft()
        if current_point == K:
            return time[current_point]
        for need_visit in (current_point-1, current_point+1, current_point*2):
            if (100001>need_visit>=0) and not (time[need_visit]) :
            #if (100001>need_visit>=0) & (time[need_visit] !=0)  과의 차이는?:
                time[need_visit] = time[current_point] + 1
                q.append(need_visit)
print(bfs())