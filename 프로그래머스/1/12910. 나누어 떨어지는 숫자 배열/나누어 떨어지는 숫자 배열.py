def solution(arr, divisor):
    new_arr = [i for i in arr if i % divisor == 0]
    
    if len(new_arr) > 0:
        answer = sorted(new_arr)
    else:
        answer = [-1]
    
    return answer