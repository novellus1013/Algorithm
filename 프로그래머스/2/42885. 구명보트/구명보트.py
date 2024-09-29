def solution(people, limit):
    answer = 0;
    
    people.sort();
    
    min = 0;
    max = len(people) - 1
    
    for i in range(len(people)):
        if min > max:
            break;
            
        if people[min] + people[max] <= limit:
            min += 1;
            max -= 1;
        else:
            max -= 1;
        answer += 1;
        
    return answer;
         
#     for i in reverse_people:
#         for j in range(0, len(people)-1):
#             if people[i] + people[j] <= limit:
#                 idx.add(i);
#                 idx.add(j);
                
#     list_idx = list(idx);         
    
#     if len(list_idx) == 0:
#         answer = len(people);
#     else:
#         answer = len(people) - len(list_idx) + len(list_idx)/2;            
    
#     return int(answer);