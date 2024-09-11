def solution(msg):
    answer = []
    new_dic = {}
    
    # A - Z 까지 포함된 사전
    for x in range(65, 91):
        new_dic[chr(x)] = x - 64 

    count = 0
    # 사전에 글자 추가
    while count < len(msg):
        word = msg[count]
        
        #현재 입력과 일치하는 가장 긴 문자열 word
        for i in range(count + 1, len(msg) + 1):
            if msg[count:i] in new_dic:
                word = msg[count:i]
            else:
                break;
        
        # new_dic에 존재하는 word의 value를 answer에 추가
        answer.append(new_dic[word])
        
        # new_dic에 없는 word를 사전에 추가
        if count + len(word) < len(msg):
            new_dic[msg[count:count + len(word) + 1]] = len(new_dic) + 1
        
        count += len(word)
        
    return answer
    
# 
# ord('A') = 65. 해당 하는 문자열 한 개 를 ord()로 감싸고 - 64 하면 색인번호
# new_dic을 만들고 새로운 단어 추가 -> new_dic[i]번째 글자의 색인은 i+27
# 문자열 i가 사전에 존재하면, i+1,i+2,... 사전에 존재하는지 확인해보고 i+n개가 존재하면 i+n의 index를 answer에 출력하고, new_dic에 i+n+c 추가

# 사전을 27~끝가지 뒤에서부터 순회 -> 만약 뒤에서부터 순회할 때 해당 원소와 겹치는 문자열이 존재한다면 msg에서 삭제



# 실패1
# A - Z 까지 포함된 사전
    # for x in range(65, 91):
    #     new_dic.append(chr(x))
#    for i in msg:
#         if i != len(msg) -1:
#             word = msg[i] + msg[i+1]
            
#             if new_dic.count(word) == 0:
#                 index1 = ord(msg[i]) - 64
#                 answer.append(index1)
#             else:
#                 index2 = new_dic.index(word) + 27
#                 answer.append(index2)


# 실패2
    # wc의 길이가 2글자이면서, 사전에 포함되어있지 않을 때 한 글자 w를 answer로 출력하고 wc를 사전에 추가 
    #     elif new_dic.count(word) == 0 and len(word) == 2: 
    #          new_dic.append(msg[count])
    #          answer.append(ord(msg[count]) - 64)
    #     # wc로 만들어진 가장 긴 글자를(2글자 이상) 구하고 사전에 포함
    #     else :
    #         new_index = new_dic.index(word) + 1
    #         new_dic.append(word)
    #         answer.append(new_index)
    # count += 1     
    
# 실패3
# for i in range(len(msg)+1):
#         word = msg[i]
#         count = i + 1
        
        
#         if word == msg[i:len(msg)]:
#             answer.append(new_dic[word])
#             return answer
#         elif word in new_dic:
#             word += word[count]
#             count += 1
#         else:
#             new_dic[word] = len(msg) + 1
#             answer.append(new_dic[word])
                
#     return answer
