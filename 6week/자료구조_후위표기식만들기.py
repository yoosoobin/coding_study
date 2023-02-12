import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

arr = list(input())
res = ''
stack=[]
for i in arr:
    if i.isdecimal():
        res += i
    else:
        if i=='(':
            stack.append(i)
        elif i=='*' or i=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res += stack.pop()
            stack.append(i)
        elif i=='+' or i=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(i)
        elif i==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()

while stack:
    res+=stack.pop()

print(res)

        







    




