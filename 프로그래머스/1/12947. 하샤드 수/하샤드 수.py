def solution(x):
    num = 0
    
    num = sum([int(i) for i in str(x)])
    
    return x % num == 0