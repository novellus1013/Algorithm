def solution(cacheSize, cities):
    #1
    answer = 0
    cache = []
    
    for city in cities:
        #2
        city = city.lower()
        
        #3-1
        if city in cache:
            answer += 1
            cache.remove(city)
        #3-2
        else:
            answer += 5

        #4    
        cache.append(city)
        
        #5
        if len(cache) > cacheSize:
            cache.pop(0)
            
    return answer

#1. 캐시를 저장할 빈 배열을 생성한다.
#2. cities의 원소들을 대소문자 상관 없도록 소문자로 일원화한다.
#3-1. cities의 원소들을 순회하면서 해당 원소가 캐시 배열에 존재한다면 answer에 1을 더하고 해당 값을 제거한다.
#3-2. cities의 원소들을 순회하면서 해당 원소가 캐시 배열에 존재하지 않는다면 answer에 5를 더한다.
#4. cities의 원소를 캐시 배열 가장 끝에 추가한다.
#5. 캐시 배열의 길이가 cacheSize보다 클 때, 캐시 배열에 가장 오래된 값인 맨 앞의 값을 제거한다.