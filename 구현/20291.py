N = int(input())
result = {}
for n in range(N):
    file_name,file_extension = input().split(".")
    if result.get(file_extension) is None:
        result[file_extension] =1
    else:
        result[file_extension] +=1
result = dict(sorted(result.items()))
for key,value in result.items():
    print(key,value)