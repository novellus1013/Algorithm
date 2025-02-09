def solution(triangle):
    length = len(triangle)
    
    
    dp = [[0] * length for _ in range(length)]
    dp[0][0] = triangle[0][0]
    
    for i in range(length - 1): 
        for j in range(i + 1): 
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])     
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
    
    return max(dp[-1])