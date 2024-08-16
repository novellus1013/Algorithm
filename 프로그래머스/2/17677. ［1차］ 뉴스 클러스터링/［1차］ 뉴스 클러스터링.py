from collections import Counter

def solution(str1, str2):
    # 1. 입력된 문자열을 전처리
    str1 = isAlpha(str1)
    str2 = isAlpha(str2)
    
    # 2. 두 글자씩 끊어서 다중집합을 생성
    new1 = multiSet(str1)
    new2 = multiSet(str2)
    
    # 3. 교집합과 합집합 계산
    counter1 = Counter(new1)
    counter2 = Counter(new2)
    
    intersection = list((counter1 & counter2).elements())  # 교집합
    union = list((counter1 | counter2).elements())         # 합집합
    
    # 4. 자카드 유사도 계산
    if len(union) == 0:
        similarity = 1
    else:
        similarity = len(intersection) / len(union)
    
    # 5. 결과 계산
    answer = int(similarity * 65536)
    
    return answer

# 영문자만 남기고 소문자로 변환하는 함수
def isAlpha(text):
    # 전체 문자열에서 영문자가 아닌 문자는 제거하고, 소문자로 변환한 후 반환
    return ''.join([item.lower() for item in text])

# 다중집합을 만드는 함수
def multiSet(text):
    multiset = []
    for x in range(len(text) - 1):
        pair = text[x:x+2]
        if pair.isalpha():  # 두 글자 모두 알파벳인 경우만 다중집합에 추가
            multiset.append(pair)
    return multiset

#1. 입력된 문자열 str1과 str2에서 영문자만 남기고 다른 값을 모두 제거한다.
#2. 바뀐 str1과 str2 를 소문자로 변경한다.
#3. 두 문자열을 두 글자씩 끊어서 다중집합의 원소를 가지는 new1, new2를 만든다.
#4. new1과 new2의 합집합, 교집합을 구한다.
#5. 자카드 유사도(합집합 - 교집합) similarity를 구한다.
#6. 두 문자의 자카드 유사도 similarity에 65536을 곱한 후 소수점 아래를 버리고 정수부만 출력

# 알게된 것 : 문자열 슬라이싱(text[x:x+2], range활용)


# 실패 1
# index = 1
#     for x in str1:
#         if(len(str1) == 2):
#             items = str1[0] + str1[1] 
#             new1.append(items)
#         elif(x != str1[len(str1) - 1]):
#             items = x + str1[index]
#             index += 1
#             new1.append(items)        
        
#     for y in str2:
#         if(len(str2) == 2):
#             items = str2[0] + str2[1]
#             new1.append(items)
#         elif(y != str2[len(str2) - 1]):
#             items = y + str2[index]
#             index += 1
#             new2.append(items)   
    
#     return new1
