def solution(a, b):
    answer = 0
    
    if a>b:
        answer = sum([i for i in range(b, a+1)])
    elif a<b:
        answer = sum([x for x in range(a, b+1)])
    else:
        answer = a
    
    return answer