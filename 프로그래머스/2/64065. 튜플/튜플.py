from collections import Counter

def solution(s):
    answer = []
    
    s1 = s[1:-1]
    s2 = s1.replace("{", "")
    s3 = s2.replace("}", "")
    s4 = s3.split(",")
    
    int_list = [int(num) for num in s4]
    
    counter = Counter(int_list)
    
    list_length = len(int_list)
    
    base_num = 1
    add_num = 0
    
    while add_num < list_length:
        add_num += base_num
        if add_num == list_length:
            break
        base_num += 1
        
    while base_num > 0:
        for item, count in counter.items():
            if count == base_num:
                answer.append(item)
                counter[item] = 0
                base_num -= 1
                break
    
    return answer

#1. s의 모든 원소를 원소로 가지는 배열 s_list를 선언
#2. s_set = set(s_list) 를 선언 => s_list의 원소들을 중복되지 않게 가지는 집합  
#3. answer = list(s_set)으로 s_set 집합 자료형의 모든 원소를 가지는 배열로 반환

# 실패1
# s_str= ''.join(map(str, s))
# s_str2 = s_str.replace("}", "")
# s_str3 = s_str2.replace("{", "")
    
# 실패 2
#     s_list = []
    
#     for items in s:
#         for item in items:
#             s_list.append(item)
    
#     s_set = set(s_list)
    
#     answer = list(s_set)
# 실패3
#     s1 = s[1: -1].replace("{", "")
#     s2 = s1.replace("}", "")
#     s3 = s2.split(",")
    
#     answer = []
    
#     for item in s3:
#         if answer.count(int(item)) == 0:
#             answer.append(int(item))

# 실패 4
# for x in int_list:
#     if int_list.count(x) == base_num:
#         answer.append(x)
#         int_list = [x2 for x2 int_list if x2 != x]
#         base_num -= 1
#     elif base_num == 0 :
#         break;

# 실패5
#     answer = []
#     s1 = s[1: -1]
#     s2 = s1.replace("{", "")
#     s3 = s2.replace("}", "")
#     s4 = s3.split(",")
    
#     int_list = [int(num) for num in s4]
    
#     list_length = len(int_list)
    
#     base_num = 1
#     add_num = 0
    
#     while add_num < list_length:
#         add_num += base_num
#         if add_num == list_length:
#             break
#         base_num += 1
        
#     while base_num > 0:
#         for item in int_list:
#             if int_list.count(item) == base_num:
#                 answer.append(item)
#                 int_list = [x for x in int_list if x != item]
#                 base_num -= 1
#                 break
    
#     return answer