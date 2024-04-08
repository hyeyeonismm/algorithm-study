def solution(array, n):
    answer = 0
    min_val=101
    array.sort()
    for i in array:
        if min_val > abs(n-i):
            min_val = abs(n-i)
            answer=i
    return answer