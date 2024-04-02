def solution(arr):
    answer = []
    if 2 not in arr:
        answer.append(-1)
        return answer

    return arr[arr.index(2):len(arr)-arr[::-1].index(2)]

    