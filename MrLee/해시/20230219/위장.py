def solution(clothes):
    answer = 1
    
    clothes_dict = {}
    for item, cat in clothes:
        if clothes_dict.get(cat) == None:
            clothes_dict[cat] = 1
        else:
            clothes_dict[cat] +=1
    for k, v in clothes_dict.items():
        answer *= (v+1)
    
    answer -=1
    return answer