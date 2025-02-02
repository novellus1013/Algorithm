def solution(citations):
    citations.sort()
    low, high = 0, len(citations)
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        count = sum(1 for x in citations if x >= mid)
        
        if count >= mid:
            low = mid + 1
        else:
            high = mid - 1

    answer = high
    return answer