def solution(k, m, score):
    # 1
    score.sort(reverse=True)
    
    # 2
    answer = 0
    for i in range(0, len(score) - m + 1, m):
        # 3
        answer += score[i + m - 1] * m
    
    return answer



# 1. score를 내림차순으로 정렬한다.
# 2. score에서부터 m개씩 원소를 가지는 상자들을 구한다.
# 3. 상자들을 순회화면서 각 상자의 가장 마지막 항 x m 을 구해 answer에 더한다. 
