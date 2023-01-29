import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0 for i in range(n + 1)] # Memoization
arr[1] = 1
for i in range(2, n + 1):
    arr[i] = arr[i - 1] * i # Factorial
print(arr[n] // (arr[m] * arr[n - m]))