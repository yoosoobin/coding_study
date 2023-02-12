N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = [0] * (N+M)
i=j=k=0
while (i<N) | (j<M):
    if (i<N) & (j==M): # A만 남은 경우
        result[k] = A[i]
        i+=1
    elif (i==N) & (j<M): # B만 남은 경우
        result[k] = B[j]
        j+=1
    if (i<N) & (j<M):
        if A[i]<=B[j]:
            result[k] = A[i]
            i+=1
        else:
            result[k] = B[j]
            j+=1
    k+=1
for i in result:
    print(i, end = " ")