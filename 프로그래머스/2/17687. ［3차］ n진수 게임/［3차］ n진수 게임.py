def solution(n, t, m, p):
    answer = ''
    total = ''
    
    # n진법 출력 함수
    for i in range(0, m*t):
        if i == 0:
            total += "0"
        else:
            word = ""
            current = i
            
            while current > 0:
                remainder = current % n
                if remainder >= 10:
                    word = chr(remainder - 10 + ord('A')) + word
                else:
                    word = str(remainder) + word
                current //= n
            
            total += word
        
    answer = total[p-1: p + m*t-m: m]
        
    return answer
# 1. 진법에 맞게 숫자 변환하기
# 2. 변환한 숫자 문자열 all에 더하기
# 3. 더한 all 에서 (p-1), (p-1)+m, p-1+2m..p +m*(t-1) 순으로 문자열 구해서 answer에 더하기
# 4. answer 출력