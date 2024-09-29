def solution(n, lost, reserve):
    answer = 0
    
    lost.sort();
    reserve.sort();
    
    for i in reserve[:]:
        if i in lost[:]:
            reserve.remove(i)
            lost.remove(i)
    
    for j in lost[:]:
        if j - 1 in reserve[:]:
            lost.remove(j)
            reserve.remove(j - 1)
        elif j + 1 in reserve[:]:
            lost.remove(j)
            reserve.remove(j + 1)
        else:
            continue;
            
    answer = n - len(lost);    
            
    return  answer