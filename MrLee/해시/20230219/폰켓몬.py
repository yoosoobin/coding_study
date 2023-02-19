def solution(nums):
    pon_dict = {}
    for i in nums:
        if pon_dict.get(i) == None:
            pon_dict[i] = 0
        else:
            pon_dict[i] +=1
    
    answer = min(len(pon_dict.keys()), len(nums)//2)
    
    return answer