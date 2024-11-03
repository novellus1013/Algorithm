from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque([begin])
    
    if target not in words:
        return 0
    
    while q:
        for _ in range(len(q)):
            current = q.popleft()
            
            if current == target:
                return answer
            
            for word in words:
                differences = sum(c1 != c2 for c1, c2 in zip(current, word))
                if differences == 1:
                    q.append(word)
        
        answer += 1
    
    return 0

# sudo
# 1. target이 words에 없을 경우 0을 반환
# 2. 큐에 추가될 글자는 current를 구성하는 원소 중 단 하나만 제외하고 모두 같아야 한다.
# 2-1. words를 순회하면서, 조건 2를 만족시키는 글자 word가 존재한다면 word를 큐에 추가하고 
# 2-2. 2-1 의 조건을 만족시키는 word를 words에서 배제한다.
# 3. current가 변경될 때마다 answer 값을 추가한다.
# 4. 조건 1과 2를 모두 만족시키지 못하는 경우 0을 반환한다.