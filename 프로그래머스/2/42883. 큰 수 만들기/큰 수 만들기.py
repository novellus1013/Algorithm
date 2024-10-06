from collections import deque

def solution(number, k):
    dq = deque();

    for num in number:
        while dq and k > 0 and dq[-1] < num:
            dq.pop();
            k -= 1;
        dq.append(num);
    
    while k > 0:
        dq.pop();
        k -= 1;
    
    answer = ''.join(dq)
    
    return answer;
    
# 실패1
#     numbers = list(map(int,number));
    
#     numbers.sort(reverse=True);
    
#     for i in range(0, len(numbers) - k):
#         answer += str(numbers[i]);
    
#     return answer


# 실패2
#     answer_list = [];
#     length = len(number) - k;
#     start = 0;
    
#     for i in range(length):
#         max = 0;
        
#         for j in range(start, i+k+1):
#             if int(number[j]) > max:
#                 max = int(number[j])
#                 start = j+1;
                
#         answer_list.append(max);
    
#     for x in answer_list:
#         answer += str(x);
                
#     return answer;