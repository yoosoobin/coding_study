def solution(genres, plays):
    answer = []
    count_dict = {}
    cat_dict = {}
    for i in range(len(genres)):
        if count_dict.get(genres[i]) == None:
            count_dict[genres[i]] = plays[i]
        else:
            count_dict[genres[i]] += plays[i]
        if cat_dict.get(genres[i]) == None:
                cat_dict[genres[i]] = {i:plays[i]}
        else:    
            cat_dict[genres[i]][i] = plays[i]


    count_dict = sorted(count_dict.items(), key = lambda item: item[1], reverse = True)
    for k,v in count_dict:

        temp = sorted(cat_dict[k].items(), key = lambda item: item[1], reverse = True)
        count = 0
        for key,value in temp:
            if count < 2:
                answer.append(key)
                count +=1
        
    return answer