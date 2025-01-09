import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mix = first + (second * 2)
        
        heapq.heappush(scoville, mix)
        answer += 1
    
    return answer




# from collections import deque

# def solution(scoville, K):
#     answer = 0
#     scoville.sort();
    
#     q = deque(scoville)
    
#     while q[0] < K:
        
#         if len(q) < 2:
#             return -1
        
#         first = q.popleft();
#         second = q.popleft();
#         mix = first + (second * 2)
        
#         q.append(mix)
        
#         q = deque(sorted(q))
        
#         answer += 1
        
#     return answer      
        
# sudo code
# 1. scoville 을 정렬한 후 deque인 q를 생성한다.
# 2-1. scovile의 첫번째 원소가 k 이상인 경우 바로 answer를 반환한다
# 2-2. 2-1이 아닐 경우 scoville의 첫번째 원소와 두번째 원소를 scoville에서 추출한다.
# 3. q에서 첫번째와 두번째인 원소를 추출(first, second) 한 후 mix를 만들어 기존 q에 더한다
# 4. q에 모든 원소를 순회한 후 모든 원소가 K이상이라면 반복문을 종료하고 answer를 반환한다.