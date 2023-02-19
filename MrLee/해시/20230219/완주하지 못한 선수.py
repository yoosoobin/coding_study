def solution(participant, completion):
    answer = ""
    answer_dict = {}
    for p in participant:
        if answer_dict.get(p) == None:
            answer_dict[p]=1
        else:
            answer_dict[p]+=1
    for c in completion:
        answer_dict[c]-=1
    for k,v in answer_dict.items():
        if v == 1:
            answer = k
    return answer