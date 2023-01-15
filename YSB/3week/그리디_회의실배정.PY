# 한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들
# 려고 한다. 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하
# 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 단, 회의는 한번 시작하면 중간에 중
# 단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다


import sys
sys.stdin=open("input.txt", "r")

n = int(input())
plan = [list(map(int,input().split())) for _ in range(n)]
plan.sort(key=lambda x : (x[1], x[0]))  # x[0]으로 오름차순, x[1]로 오름차순 적용
 
s,e= plan[0][0], plan[0][1]

cnt = 1
for i in plan:
    if i[0] >= e:
        cnt +=1
        e = i[1]

print(cnt)