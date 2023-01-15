#import sys
#input = sys.stdin.readline
N, X = list(map(int, input().split()))
blog_cnt = list(map(int, input().split()))

if sum(blog_cnt) == 0:
    print("SAD")

    
else:
    maximum_value = sum(blog_cnt[:X])
    value = maximum_value
    count = 1
    
    for i in range(X,N):
        value = value - blog_cnt[i-X] + blog_cnt[i]
        #print(value,maximum_value,blog_cnt[i-X],blog_cnt[i])
        #print(value, maximum_value, count)
        

        if value > maximum_value:
            maximum_value = value
            count = 0
        if value == maximum_value:
            count += 1
            
    print(maximum_value)
    print(count)