import sys
# sys.stdin = open(r'C:\Users\dbqhr\OneDrive\바탕 화면\AA\AA\input.txt','r')

n= int(input())

def func(x):
    if x!= 1:
        func(x//2)
        print(x%2,end = '')
    else: 
        print(1,end = '')

func(n)








        


