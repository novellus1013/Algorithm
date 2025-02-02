def solution(brown, yellow):
    total = brown + yellow
    
    for w in range(3, total + 1):
        if total % w == 0:
            h = total // w

            if w >= h and (w - 2) * (h - 2) == yellow:
                answer = [w, h]
                
                
    return answer
    
    
    
    
#     total = brown + yellow
    
#     first, last = 3, total
    
#     while first <= last:
#         w = (first + last) // 2
        
#         if total % w == 0:
#             h = total // w
            
#             if (w - 2) * (h - 2) == yellow:
#                 answer = [w, h]
#                 return answer
            
#             if w * h < total:  
#                 first = w + 1
#             else:
#                 last = w - 1
    