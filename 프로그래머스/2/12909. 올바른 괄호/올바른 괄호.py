def solution(s):
    answer = True
    stack = list(s)
    left = 0
    right = 0
    
    while stack and right >= left:
        parentheses = stack.pop();
        
        if parentheses == ")":
            right += 1
        else:
            left += 1
            
    if left != right or s[-1] == "(" or s[0] == ")":
        answer = False
    
    return answer