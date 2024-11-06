def solution(arr):
    answer = [arr[0]]
    
    for item in arr:
        last_item = answer[-1]; 
        if(item != last_item):
            answer.append(item);
        
    return answer