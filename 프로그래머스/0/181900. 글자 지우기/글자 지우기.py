def solution(my_string, indices):
    indices.sort()
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:
            answer+=my_string[i]
    
    return answer