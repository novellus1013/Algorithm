def solution(n, computers):
    answer = 0
    
    count = [False] * n;
    
    for i in range(n):
        if not count[i]:
            stack = [i];
            
            # 체크하지 않은 computer에 대한 처리
            while stack:
                computer = stack.pop();
                
                if not count[computer]:
                    count[computer] = True;
    
                for j in range(n):
                    if computers[computer][j] == 1 and not count[j]:
                        stack.append(j);
                            
            answer += 1;
    
    return answer