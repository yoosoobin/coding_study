N = int(input())
for i in range(N):
    stack = []
    result = "YES"
    string = input()
    for s in string:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if len(stack) != 0:
                stack.pop(-1)
            else:
                result = "NO"
                break
    
    if (len(stack) == 0) & (result != "NO"):
        result = "YES"
    else:
        result = "NO"
            
    print(result)