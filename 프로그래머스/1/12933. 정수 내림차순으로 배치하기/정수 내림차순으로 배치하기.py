def solution(n):
    numbers = [i for i in str(n)]
    numbers.sort(reverse=True)
    answer = int(''.join(numbers))
    
    return answer

# 1.정수 n을 리스트로 변경
# 2. 리스트를 내림차순으로 정렬
# 3. 리스트 -> 문자열 -> 정수 변경