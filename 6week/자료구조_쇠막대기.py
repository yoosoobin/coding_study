import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

arr = list(input())
cnt = 0
stack = []

for n,i in enumerate(arr):
    if i==')' and arr[n-1]=='(':
        stack.pop()
        cnt+=len(stack)
    elif i==')' and arr[n-1] ==')':
        stack.pop()
        cnt+=1
    else:
        stack.append(i)

print(cnt)






