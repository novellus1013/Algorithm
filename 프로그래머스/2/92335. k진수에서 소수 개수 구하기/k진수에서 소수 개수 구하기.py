def solution(n, k):
    answer = 0
    word = ''
    
    # k진수로 변환한 n의 값
    while n > 0:
        remainder = n % k
        word = str(remainder) + word
        n //= k
    
    # if word.count("0") == 0:
    #     return 1
    
    word = word.replace("0"," ").split( )
    
    new_word = [int(item) for item in word if item != "1"]
    
    for i in new_word:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                new_word.remove(i)
                break
        
    answer = len(new_word)     
    return answer
    
    
#     real_word = new_word
    
#     for i in new_word:
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 real_word = [x for x in new_word if x != i]
#                 break
    
#     return len(real_word)