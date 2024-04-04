def solution(str_list):
    answer = []
    for i in str_list:
        if i=='l':
            return str_list[:str_list.index(i)]
        elif i=='r':
            return str_list[str_list.index(i)+1:]
    else:
        return answer
        
    
    
    