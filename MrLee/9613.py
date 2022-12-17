def gcd(first,second):
    if second == 0:
        return first
    else:
        return gcd(second, first % second)

N = int(input())
for _ in range(N):
    row = list(map(int,input().split(" ")))
    n = row.pop(0)
    gcd_list = []
    for i in range(n-1):
        for j in range(i+1,n):
            gcd_list.append(gcd(row[i], row[j]))
    print(sum(gcd_list))