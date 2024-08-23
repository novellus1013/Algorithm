def solution(numbers):
    num_list = list(range(0,10))
    
    for i in numbers:
        num_list.remove(i)
        
    answer = sum(num_list)
        
        
    return answer