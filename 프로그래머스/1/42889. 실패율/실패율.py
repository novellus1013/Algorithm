def solution(N, stages):
    people = len(stages)
    kv = dict()
    
    # dictionary로 stage와 stage의 실패율을 저장
    for i in range(1, N+1):
        s_count = stages.count(i)
        if s_count == 0 :
            kv[i] = 0
        else :
            kv[i] = s_count / people
            people = people - s_count
    
    # dictionary의 values 내림차순 정렬
    kv2 = sorted(kv.items(), key=lambda item: item[1], reverse =True)
    
    # kv2에서 key 값만 뽑아서 정렬
    answer = [num for num,_ in kv2]
    
    return answer