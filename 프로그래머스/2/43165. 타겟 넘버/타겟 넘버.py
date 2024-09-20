def solution(numbers, target):
    answer = 0
    new_numbers = [[] for _ in range(len(numbers))]
    index = 0
    
    def dfs(i, total):
        if i == len(numbers):
            return ;
        
        new_numbers[i].append(total+numbers[i]);
        new_numbers[i].append(total-numbers[i]);
        
        dfs(i+1, total + numbers[i]);
        dfs(i+1, total - numbers[i]);
    
    dfs(0,0);
    
    [last_numbers] = new_numbers[-1:]
    
    for x in last_numbers:
        if x == target:
            answer += 1;
    
    return answer;