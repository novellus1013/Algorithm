from collections import deque

def solution(tickets):
    tickets.sort()
    answer = []
    visited = [False] * len(tickets)
    q = deque([("ICN", ["ICN"], visited[:])])

    while q:
        current, path, visited_state = q.popleft()
        
        if len(path) == len(tickets) + 1:
            answer = path
            break
        
        for i in range(len(tickets)):
            if not visited_state[i] and tickets[i][0] == current:
                new_visited = visited_state[:]
                new_visited[i] = True
                q.append((tickets[i][1], path + [tickets[i][1]], new_visited))
                
    return answer

