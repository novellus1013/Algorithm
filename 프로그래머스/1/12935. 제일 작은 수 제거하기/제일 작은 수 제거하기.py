def solution(arr):
    answer = []
    arr.remove(min(arr))
    
    if len(arr) > 0:
        answer = arr
    else:
        answer = [-1]
    
    return answer