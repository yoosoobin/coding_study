from math import gcd

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False  
    return True



def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]



N = int(input())
num_list = list(map(int, input().split()))

prime_list = []
for num in num_list:
    if isPrime(num):
        prime_list.append(num)

if len(prime_list) == 0:
    print(-1)
else:

    print(solution(prime_list))







