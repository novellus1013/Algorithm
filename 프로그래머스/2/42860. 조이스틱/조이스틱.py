def solution(name):
    answer = 0
    length = len(name)

    for x in name:
        answer += min(ord(x) - ord('A'), ord('Z') - ord(x) + 1)
    
    #기본 이동 거리
    move = length - 1 
    
    for current in range(length):
        next_string_index = current + 1
        
        while next_string_index < length and name[next_string_index] == 'A':
            next_string_index += 1
        # 현재 위치 + 단어 끝까지의 거리 - 선택된 글자의 위치 + 현재 위치 = 순방향 이동
        # 현재 위치 + 단어 끝까지의 거리 - 선택된 글자의 위치 + (단어의 길이 - 선택된 글자의 위치) = 역방향 이동
        move = min(move, current + length - next_string_index + min(current, length - next_string_index))

    answer += move
    return answer
