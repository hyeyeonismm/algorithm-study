def solution(num_list, n):
    answer=[]
    for j in range(0,len(num_list),n):
        answer.append([num_list[i] for i in range(j,n+j)])
    return answer