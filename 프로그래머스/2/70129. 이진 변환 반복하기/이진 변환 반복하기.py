def solution(s):
    count = 0
    num = 0
    p_text = s
    
    while p_text != "1":
        count += len(p_text)
        p_text= p_text.replace("0","")
        count -= len(p_text)
        
        p_text = bin(len(p_text))[2:]
        num += 1
        
    answer = [num, count]
    
    return answer

#1-1. 이진변환을 위한 함수 trans를 구현한다.  
#2-1. trans에 문자열 s를 입력하고 새로운 출력값 s(i)를 구한다.
#2-2. len(s) - len(s(i))을 숫자 count에 더한다.
#2-3. trans의 출력값이 1이 될때까지 반복한다.
#3. result = [i, count]를 구한다.

# 실패1
# def trans(text):
#     newText = text.remove("0")
#     result = newText