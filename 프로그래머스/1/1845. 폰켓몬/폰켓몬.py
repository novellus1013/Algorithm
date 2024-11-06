def solution(nums):
    answer = 0
    
    nums_set = set(nums);
    list_nums_set = list(nums_set);
    
    max_num = len(nums) / 2;
    type_num = len(list_nums_set);
    
    if type_num >= max_num:
        answer = max_num
    else:
        answer = type_num
    
    return answer