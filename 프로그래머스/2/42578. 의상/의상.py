def solution(clothes):
    total = {}
    answer = 1
    
    for item, category in clothes:
        if category in total:
            total[category] += 1
        else:
            total[category] = 1
    
    for x in total.values():
        answer *= (x+1)
    
    return answer - 1