#전위순회 
def DFS(v):
    if v>7:
        return 
    else:
        print(v)
        DFS(v*2) # 왼쪽 노드 호출한 것
        DFS(v*2+1) #오른쪽 노드 호출한 것


if __name__ == '__main__':
    DFS(1)

# 중위순회
def DFS(v):
    if v>7:
        return 
    else:
        DFS(v*2) # 왼쪽 노드 호출한 것
        print(v, end=' ')
        DFS(v*2+1) #오른쪽 노드 호출한 것


if __name__ == '__main__':
    DFS(1)

# 후위순회
def DFS(v):
    if v>7:
        return 
    else:
        DFS(v*2) # 왼쪽 노드 호출한 것
        DFS(v*2+1) #오른쪽 노드 호출한 것
        print(v, end=' ')


if __name__ == '__main__':
    DFS(1)

