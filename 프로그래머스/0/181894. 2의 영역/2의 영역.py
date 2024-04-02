def solution(arr):
    answer = []
    if 2 not in arr:
        answer.append(-1)
        return answer

    for i in range(len(arr)):
        if arr[i]==2:
            answer += arr[i:]
            break
    j = len(answer)-1
    while j>=0: 
        if answer[j]==2: 
            return answer[:j+1]
        j-=1