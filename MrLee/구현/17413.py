string = list(input())
tag = []
word = []
i = 0
while i<len(string):
    
    if string[i] == "<":
        while True:
            if string[i] == ">":
                tag.append(string[i])
                break
            else:
                tag.append(string[i])
                i+=1
    elif string[i].isalnum() :
        word_start = i
        while i < len(string) and string[i].isalnum():
            i+=1
        tmp = string[word_start:i]
        tmp = tmp[::-1]
        string[word_start:i] = tmp
                
    else:
        i+=1

    
print("".join(string))