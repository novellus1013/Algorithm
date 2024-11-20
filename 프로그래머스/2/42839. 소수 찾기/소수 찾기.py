from itertools import permutations

def solution(numbers):
    answer = 0
    n_list = list(numbers)
    
    total = set()
    
    for i in range(1, len(n_list) + 1):
        for x in permutations(n_list, i):
            total.add(int("".join(x)))
    
    # 소수 판별하기
    for item in total:
        if item <2:
            continue
        is_prime = True;
        for i in range(2, int(item ** 0.5) +1):
            if item % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
                
    return answer