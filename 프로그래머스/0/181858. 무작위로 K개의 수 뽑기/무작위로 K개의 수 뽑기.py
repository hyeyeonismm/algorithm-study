def solution(arr, k):
    answer = []
    for i in range(len(arr)): #3
        if arr[i] not in answer: 
            answer.append(arr[i]) #0 #1
        if len(answer)>=k:
            break
    if len(answer)<k:
        for i in range(k-len(answer)):
            answer.append(-1)
    return answer