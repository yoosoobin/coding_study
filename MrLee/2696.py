T = int(input())
for _ in range(T):
    N = int(input())
    num_list = []
    if N > 10:
        for _ in range(N//10+1):
            temp = list(map(int,input().split()))   
            num_list += temp
    else:
        num_list = list(map(int,input().split()))    
    
    print(len(num_list) // 2 + 1)
    median = []
    count = 0
    for i,n in enumerate(num_list):
        median.append(n)
        if i % 2 == 0:
            
            median_index = i//2
            median_sort = sorted(median)
            print(median_sort[median_index], end = " ")
            count += 1
            if count % 10 == 0:
                print()            
             
    print()