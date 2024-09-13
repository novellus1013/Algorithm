def solution(numbers):
    answer = []
    
    my_set = set();
    
    for i in range(0, len(numbers)):
        nums = 1;
        while i+nums < len(numbers):
            total = numbers[i] + numbers[i+nums];
            my_set.add(total);
            nums += 1;
    
    answer = list(my_set);
    answer.sort();
    
    return answer;