import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

n,m = map(int,input().split())
tmp = list(map(int,str(n)))
stack = []

for x in tmp:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack = stack[:-m]

res = ''.join(map(str,stack))
print(res)

    






