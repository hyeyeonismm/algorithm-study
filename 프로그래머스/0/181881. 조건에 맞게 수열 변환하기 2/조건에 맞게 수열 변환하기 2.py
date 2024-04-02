def solution(arr):
    tmp = 0
    count = 0
    answer = []
    answer += arr
    while tmp != len(arr):
        tmp = 0
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = (arr[i] * 2) + 1
            else:
                tmp += 1
        count+=1
    else:
        return count-1