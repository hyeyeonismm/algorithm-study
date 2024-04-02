def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        strArr[i] = len(strArr[i])
    answer=[0] * (max(strArr)+1)
    
    for i in range(len(strArr)):
        answer[strArr[i]]+=1

    return max(answer)