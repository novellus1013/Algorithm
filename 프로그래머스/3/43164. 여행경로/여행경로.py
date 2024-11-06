def solution(tickets):
    tickets.sort()
    answer = []
    visited = [False] * len(tickets)
    stack = [("ICN", ["ICN"], visited)]

    while stack:
        current, path, visited_state = stack.pop()
        
        if len(path) == len(tickets) + 1:
            answer = path
            break
        
        for i in range(len(tickets) -1, -1, -1):
            if not visited_state[i] and tickets[i][0] == current:
                new_visited = visited_state[:]
                new_visited[i] = True
                stack.append((tickets[i][1], path + [tickets[i][1]], new_visited))
                
    return answer

