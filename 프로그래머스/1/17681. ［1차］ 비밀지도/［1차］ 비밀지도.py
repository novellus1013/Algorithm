def solution(n, arr1, arr2):
    answer = []
    
    # 2진수로 변환
    arr1 = [bin(i)[2:] for i in arr1]
    arr2 = [bin(i)[2:] for i in arr2]
    
    # n의 길이만큼 모든 값이 벽과 공백을 나타내도록 0을 가지게 변환 (조건3)
    arr1 = ["0" * (n - len(i)) + i if len(i) != n else i for i in arr1]
    arr2 = ["0" * (n - len(i)) + i if len(i) != n else i for i in arr2]
            
    # 이중 for문으로 arr1과 arr2의 값이 모두 0이면 공백, 아니면 벽을 추가
    for i in range(0, n):
        maps = ""
        
        for y in range(0, n):
            
            if arr1[i][y] == "0" and arr2[i][y] == "0":
                maps += " "
            else:
                maps += "#"
            
        answer.append(maps)
                
    return answer