def solution(n, m, section):
    num = section[0]
    answer = 1
    
    if m == 1:
        return len(section)
    
    if len(section) == 1:
        return 1
    
    for i in section:
        if num + m <= i:
            num = i
            answer +=1
    return answer 
    
    
# 실패1
#     num = section[0]
#     answer = 1
    
#     for i in section:
#         if m == 1:
#             answer = len(section)
#         elif num + m -1 <= i:
#             num = i
#             answer +=1 
#     return answer


# 실패2
#     first = section[0]
#     last = section[-1]
#     answer = 1
    
#     for i in section:
#         if m == 1:
#             answer = len(section)
#         elif (last - first + 1) % m == 0:
#             answer = (last - first +1) /m
#         else:
#             answer = (last-first +1) // m +1
#     return answer


# 실패3
    # space = section[-1] - section[0] + 1
    # for i in section:
    #     # m이 1일 경우 section의 길이가 횟수
    #     if m == 1:
    #         answer = len(section)
    #     # section의 길이가 1인 경우 m의 쵯솟값도 1이기 때문에 1
    #     elif len(section) == 1:
    #         answer = 1
    #     # section의 최댓값과 최솟값의 차이가 m보다 작거나 같다면 1
    #     elif space <= m:
    #         answer = 1
    #     # 
    #     elif space % m == 0:
    #         answer = space / m
    #     else:
    #         answer = space//m + 1
    # return answer