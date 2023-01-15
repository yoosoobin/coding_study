N = int(input())

def snail(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    points = {}
    row = -1
    col = 0
    value = n **2
    trans = 1
    while n > 0:
        for i in range(n):
            row += trans
            arr[row][col] = value
            points[value] = (row, col)
            value -= 1
        n -= 1
        for j in range(n):
            col += trans
            #import pdb; pdb.set_trace()
            arr[row][col] = value
            points[value] = (row, col)
            value -= 1
        
        trans *= -1
    return arr, points

arr, points = snail(N)
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
M = int(input())
x, y = points[M]
print(x+1, y+1)
