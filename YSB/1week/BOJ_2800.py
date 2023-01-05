# 괄호 제거 (2800)
# https://www.acmicpc.net/problem/2800
# https://hyem-study.tistory.com/40   (combination 관련 설명)

import sys
from itertools import combinations

# input = sys.stdin.readline
# s = input().rstrip()

str ='(0/(0))'
n = list(str)
answer = set()
stack = []
temp = []

# 반복문을 통해 괄호의 시작점과 끝점을 저장
for idx, word in enumerate(n):
    if word == "(":
        stack.append(idx)
    elif word == ")":
        temp.append((stack.pop(), idx))

print(temp)
print(len(temp))
for i in range(1, len(temp) + 1):
    c = combinations(temp, i) # combinations을 통해 모든 경우의 수를 확인 (c에는 조합 객체가 담김)
    
    # 반복문을 통해 경우의 수를 확인
    for j in c:
        target = list(n) #str을 리스트로 변환, target reset

        # 괄호 제거
        print('j',j)
        for k in j:
            print('k',k)
            target[k[0]] = "" #해당 인덱스 괄호를 제거 
            target[k[1]] = ""

        answer.add(''.join(target))

for ans in sorted(list(answer)):
    print(ans)