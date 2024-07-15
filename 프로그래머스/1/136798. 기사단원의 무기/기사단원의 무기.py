def solution(number, limit, power):
    # 1
    count = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            count[j] += 1

    # 2
    low_limit = sum(x for x in count if x <= limit)

    # 3
    over_limit = sum(1 for x in count if x > limit)

    # 4
    result = low_limit + over_limit * power

    return result




# 1. 1부터 number까지의 모든 수의 약수를 원소로 가지는 배열 count를 정의
# 2. count의 원소 중 limit을 넘지 않는 수를 모두 더한 low_limit을 정의
# 3. count의 원소 중 limit을 넘는 않는 수의 갯수인 over_limit을 정의
# 4. low_limit + over_limit*power = result를 구함  