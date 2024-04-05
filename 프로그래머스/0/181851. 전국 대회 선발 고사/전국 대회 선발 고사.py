def solution(rank, attendance):
    answer=[]
    res=0
    for i in range(len(rank)):
        if attendance[i]==True:
            answer.append([rank[i],i])
    answer.sort()
    res = 10000* answer[0][1] + 100 * answer[1][1] + answer[2][1]
    return res