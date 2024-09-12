def solution(a, b):
    answer = ''
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'] 
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    
    total_month = 0
    for i in range(0, len(month)):
        if i < a :
            total_month += month[i]
    
    remain = (total_month + b) % 7
    
    answer = day[remain]
    
    return answer