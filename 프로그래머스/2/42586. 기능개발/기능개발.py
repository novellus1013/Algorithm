from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    progress_q = deque(progresses)
    speeds_q = deque(speeds)

    
    while progress_q and speeds_q:
        progress = progress_q.popleft();
        speed = speeds_q.popleft();
        last = 100 - progress
        multi = math.ceil(last / speed)
        
        item = 1
        while progress_q and progress_q[0] + speeds_q[0] * multi >= 100:
            progress_q.popleft()
            speeds_q.popleft()
            item += 1
        
        answer.append(item)
    
    return answer