from collections import deque;

def solution(maps):
    n = len(maps);
    m = len(maps[0]);  
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    q = deque([(0, 0)]);
    
    while q:
        x, y = q.popleft();
        
        # x, y가 목표지점에 도달했다면 maps[x][y] return
        if x == n-1 and y == m-1:
            return maps[x][y]
        
        # directions에서 추가할 수 있는 방향은 4개
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            
            # directions가 추가된 행, 열이 n x m 범위 안에 있고 이동한 장소가 1일 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx,ny))
                # 이동한 거리 + 시작지점까지 칸수를 더해야 하므로 maps[0][0] = 1에서 이동할때마다 거리가 1씩 증가
                maps[nx][ny] = maps[x][y] + 1
    
    return - 1
