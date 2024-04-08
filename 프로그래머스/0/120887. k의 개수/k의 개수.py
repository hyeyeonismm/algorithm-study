def solution(i, j, k):
    answer = 0
    for sn in range(i,j+1):
        answer += str(sn).count(str(k))
    return answer