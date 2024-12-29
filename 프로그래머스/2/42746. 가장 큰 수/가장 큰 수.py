def solution(numbers):
    str_n = [str(x) for x in numbers];
    
    str_n.sort(key=lambda x: x*3, reverse=True)
    
    if str_n[0] == '0':
        return '0'
    else:
        return ''.join(str_n)
    
# 시간 초과 오류    
#     n = len(str_n)
    
    
#     for i in range(n):
#         for j in range(n - 1 - i):
#             if str_n[j] + str_n[j + 1] < str_n[j+1] + str_n[j]:
#                 str_n[j], str_n[j + 1] = str_n[j + 1], str_n[j]
    
#     for x in str_n:
#         answer += x
        
    
#     return answer