def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
        
    return answer

    # return [i for i in range(x, x*(n+1), x)]
