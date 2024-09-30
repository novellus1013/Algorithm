from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    queue = deque(people)

    while queue:
        person = queue.pop()
        if len(queue) > 0 and person + queue[0] <= limit:
            queue.popleft()
        answer += 1
    return answer

         
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